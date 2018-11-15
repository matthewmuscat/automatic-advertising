import re
import urllib
import psycopg2
import smtplib
import sqlite3
from collections import deque
from urllib.parse import urlsplit
from unicodedata import normalize
import string
from sqlite3 import Error
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import chardet
import requests
import requests.exceptions
import traceback
#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config import DBHOST, DBNAME, DBPASS, DBUSER

## INIT ##
browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# chrome_options = Options()  
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--headless')
# browser = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=chrome_options)
# browser.get('https://www.google.com/')


results = {}
search_category_list = ['Accommodation', 'hairdresser', 'engineering', 'restaurants'] 
search_location_list = ['Mackay QLD', 'Greater Brisbane, QLD', 'Townsville, QLD', 'Tasmania']
dbname = DBNAME 
dbuser = DBUSER 
dbhost = DBHOST 
dbpass = DBPASS 


################# DETERMINE FUNCTIONS #####################

""" create a database connection to a SQLite database """

try:
    conn = psycopg2.connect(dbname=dbname, user=dbuser, host=dbhost, password=dbpass)
    print("im connected")
except psycopg2.Error as e:
    print("I am unable to connect to the database")
    print(e)
    print(e.pgcode)
    print(e.pgerror)
    print(traceback.format_exc())

cursor = conn.cursor()


def get_contact_info(contact_class, div, attribute='href'):
    try:
        return div.find_element_by_class_name(contact_class).get_attribute(attribute)
    except:
        return None


def get_business_name(contact_class, div):
    try:
        return div.find_element_by_class_name(contact_class).text
    except:
        return None

def get_search(contact_class, div, attribute='value'):
    try:
        return div.find_element_by_class_name(contact_class).get_attribute(attribute)
    except NoSuchElementException:
        return None

def next_page():
    element = browser.find_element_by_css_selector('div.button-pagination-container a.navigation:last-of-type').get_attribute('href')
    browser.get(element)

def generate_url_name(business_name):
    normalised_text = normalize('NFD', business_name)
    url = normalised_text.lower()
    url_link = ""
    for character in url:
        if character.islower():
            url_link += character
        elif character == " ":
            url_link += "_"
        elif character == "&":
            url_link += "and"
        else:
            continue
    return url_link

def is_ascii(variable):
    try:
        variable.encode('ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True  # string is ascii

def check_button_exists(contact_class, attribute='href'):
    try:
        browser.find_element_by_css_selector(contact_class).get_attribute(attribute)
    except NoSuchElementException:
        return False
    return True

def search(category, location):
    cat = urllib.parse.quote(category)
    loc = urllib.parse.quote(location)
    browser.get(f'https://www.yellowpages.com.au/search/listings?clue={cat}&locationClue={loc}')

def store_dict(cursor):
    create_table(cursor)
    for business_name in results:  # how to get the business name
        website = results[business_name]['website']
        email = results[business_name]['email']
        location = results[business_name]['location']
        phone = results[business_name]['phone']
        type = results[business_name]['type']
        logo = results[business_name]['logo']
        url = generate_url_name(business_name)
        if not duplicate_check(cursor, business_name, email):
            cursor.execute("INSERT INTO listings(business_name, website, email, phone, location, type, logo, url) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", (business_name, website, email, phone, location, type, logo, url))
            conn.commit()
    conn.close()

def create_table(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS listings (
                            business_name text,
                            website text,
                            email text,
                            phone text,
                            location text,
                            type text,
                            logo text,
                            url text,
                            sent int DEFAULT 0
                        ); """)
    blacklist(cursor, ["Roshni Indian Restaurant", "Mackay Entertainment & Convention Centre"], ["bookings@roshni.com.au", "mecc@mackay.qld.gov.au"])  # BLACKLIST {name}, {email}


def duplicate_check(cursor, name, email):
    name = cursor.execute("SELECT business_name FROM listings WHERE business_name=%s;", (name,))
    email = cursor.execute("SELECT business_name FROM listings WHERE email=%s;", (email,))

    if name or email:
        return True
    return False


def blacklist(cursor, names: list, emails: list):
    for name, email in zip(names, emails):
        name_exists = cursor.execute("SELECT business_name FROM listings WHERE business_name=%s;", (name,))
        email_exists = cursor.execute("SELECT business_name FROM listings WHERE email=%s;", (email,))
        if name_exists:
            name_exists.fetchone()
        if email_exists:
            email_exists.fetchone()
        if name_exists or email_exists:
            if name_exists == email_exists:
                cursor.execute("UPDATE listings SET sent = 1 WHERE business_name = %s", (name,))
            else:
                cursor.execute("UPDATE listings SET sent = 1 WHERE business_name = %s OR email = %s", (name, email))
        else:
            cursor.execute(
                "INSERT INTO listings(business_name, email, sent) VALUES(%s, %s, %s)", (name, email, "1"))
            conn.commit()

################# SCRAPE #####################

for location in search_location_list:
    for category in search_category_list:
        search(category, location)

        # loop until there are no more pages
        while True:
            listing_divs = browser.find_elements_by_class_name('search-contact-card-table-div')

            # sort through contact divs - fetch data
            for div in listing_divs:
                business_info = {}

                logo = get_contact_info('listing-logo', div, attribute='src')
                if logo:
                    business_info['logo'] = logo
                else:
                    business_info['logo'] = ""

                phone = get_business_name('contact-text', div)
                business_info['phone'] = phone

                business_info['location'] = location
                business_info['type'] = category

                # Get website
                website = get_contact_info('contact-url', div, attribute='href')
                if website:
                    business_info['website'] = website
                else:
                    business_info['website'] = ""

                # Get email
                email = get_contact_info('contact-email', div, attribute='data-email')
                if email:
                    business_info['email'] = email
                else:
                    continue

                # Get business name
                name = get_business_name('listing-name', div)
                if name:
                    if is_ascii(name):
                        results[name] = business_info

            # if the next button exists, move to the next page.
            if check_button_exists('div.button-pagination-container a.navigation:last-of-type', attribute='href'):
                # next_butt
                # on_exists = True
                next_page()
            else:
                break

store_dict(cursor)