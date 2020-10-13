import requests
import requests.exceptions
import psycopg2
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import traceback
from config import MAILGUN_URL, MAILGUN_SENDER, MAILGUN_KEY, DBHOST, DBNAME, DBPASS, DBUSER, EMAIL, EMAILPASS
from email_config import email_message_template, email_subject_template, email_message_template_text, email_subject_if_sent, email_msg_if_sent
import smtplib

_email = EMAIL 
_emailpass = EMAILPASS

# Initialise Database Connection
try:
  conn = psycopg2.connect(dbname=DBNAME, user=DBUSER, host=DBHOST, password=DBPASS)
except psycopg2.Error as e:
  print(e)

cursor = conn.cursor()

def fetch_businesses(cursor, number):
  cursor.execute("SELECT * FROM listings WHERE sent = 0 ORDER BY type LIMIT %s;", (number,))  
  fetch_listings = cursor.fetchall()
  # unpack the listings into a dictionary
  listings = []
  type_var = None
  for list_element in fetch_listings:
    results_dict = {}
    business_name = list_element[0]
    website = list_element[1]
    email = list_element[2]
    phone = list_element[3]
    location = list_element[4]
    type = list_element[5]
    logo = list_element[6]
    url = list_element[7]
    sent = list_element[8]

    if not type_var or type_var == type:
      type_var = type
    else:
      break

    results_dict['business_name'] = business_name
    results_dict['website'] = website
    results_dict['email'] = email
    results_dict['phone'] = phone
    results_dict['location'] = location
    results_dict['type'] = type
    results_dict['logo'] = logo
    results_dict['url'] = url
    results_dict['sent'] = sent
    listings.append(results_dict)

  return listings

def send_email_gmail(name, email, website, has_website, location, type, demo):
  msg = MIMEMultipart()
  msg['From'] = 'Matthew Muscat'
  msg['To'] = email
  msg['Subject'] = email_subject_template(name, website, has_website)
  message = email_message_template(name, website, has_website, location, type, demo)
  msg.attach(MIMEText(message, 'html')) #, 'html' for html email!

  mailserver = smtplib.SMTP('smtp.gmail.com', 587)
  # identify ourselves to smtp gmail client
  mailserver.ehlo()
  # secure our email with tls encryption
  mailserver.starttls()
  # re-identify ourselves as an encrypted connection
  mailserver.ehlo()
  mailserver.login(_email, _emailpass)
  mailserver.sendmail(_email, email, msg.as_string())
  mailserver.quit()

def mailgun_send(name, email, website, has_website, location, type, demo):
  return requests.post(
    MAILGUN_URL,
    auth=("api", MAILGUN_KEY),
    data={"from": MAILGUN_SENDER,
          "to": email,
          "subject": email_subject_template(name, website, has_website),
          "html": email_message_template(name, website, has_website, location, type, demo)}) # ,
          #"text": email_message_template(name, website, has_website, location, type, demo)})

def email_if_sent_gmail(name, email):
  msg = MIMEMultipart()
  msg['From'] = 'Matthew Muscat'
  msg['To'] = email
  msg['Subject'] = email_subject_if_sent()
  message = email_msg_if_sent(name)
  msg.attach(MIMEText(message, 'html')) #, 'html' for html email!

  mailserver = smtplib.SMTP('smtp.gmail.com', 587)
  # identify ourselves to smtp gmail client
  mailserver.ehlo()
  # secure our email with tls encryption
  mailserver.starttls()
  # re-identify ourselves as an encrypted connection
  mailserver.ehlo()
  mailserver.login(_email, _emailpass)
  mailserver.sendmail(_email, email, msg.as_string())
  mailserver.quit()

def email_if_sent_mailgun(name, email):
  return requests.post(
    MAILGUN_URL,
    auth=("api", MAILGUN_KEY),
    data={"from": MAILGUN_SENDER,
          "to": email,
          "subject": email_subject_if_sent(),
          "html": email_msg_if_sent(name)}) # ,
          #"text": email_message_template(name, website, has_website, location, type, demo)})

def email_if_sent(cursor):
  cursor.execute("SELECT * FROM listings WHERE sent = 1;")
  fetch_listings = cursor.fetchall()
  # unpack the listings into a dictionary
  listings = []
  for list_element in fetch_listings:
    results_dict = {}
    business_name = list_element[0]
    email = list_element[2]
    location = list_element[4]

    results_dict['business_name'] = business_name
    results_dict['email'] = email
    results_dict['location'] = location
    listings.append(results_dict)

  for business in listings:
    #email = business['email']
    email = _email
    name = business['business_name']
    location = business['location']
    if location: # excluding blacklisted items. BLACKLISTED ITEMS MUST NOT HAVE A LOCATION IN DB
      if 'hotmail' in email or 'outlook' in email:
        print("email is hotmail/outlook")
        email_if_sent_gmail(name, email)
      else:
        print("email is not hotmail/outlook")
        email_if_sent_mailgun(name, email)
    else:
      continue

def send_email(number):
  businesses = fetch_businesses(cursor, number)
  print(businesses)
  for business in businesses:
      email = business['email']
      name = business['business_name']
      website = business['website']
      location = business['location']
      type = business['type']
      demo = "https://demo.matthewmuscat.com.au/%s" % business['url']
      if business['website'] == "":
        has_website = False
      else:
        has_website = True

      if 'hotmail' in email or 'outlook' in email:
        print("email is hotmail/outlook")
        send_email_gmail(name, email, website, has_website, location, type, demo)
      else:
        print("email is not hotmail/outlook")
        mailgun_send(name, email, website, has_website, location, type, demo)

      cursor.execute("UPDATE listings SET sent = 1 WHERE business_name = %s;", (name,))
      conn.commit()

send_email(3)               
conn.close()

