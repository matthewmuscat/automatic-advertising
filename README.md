# ✨ Automatic Advertising ✨
Completely automate your mass advertising to companies of your choosing. Filter through company types (restaurant, barber, etc) and locations to target a specific audience. Customise your website templates and email descriptions, and get to work!

### Technical Description
This tool scrapes company data on Yellow Pages which is stored in a local Postgres database. This data is then fed, on execution, dynamically into the website template of the associated company type, which is then automatically sent through Mailgun to the targeted companies. 

### Guide
``config.py`` - localized config file for Mailgun & Postgres credentials.

[Email description template configuration](https://github.com/matthewmuscat/automatic-advertising/blob/master/emailText.py)

[Sets up database, fetches company data and stores into database](https://github.com/matthewmuscat/automatic-advertising/blob/master/main.py)

[Processing stored data and fed into website templates](https://github.com/matthewmuscat/automatic-advertising/blob/master/main.py)


```python send_emails.py``` will execute the program, sending the desired amount of emails as set in the code.

### Stack
Python, Flask, Jinja2 + core Web Development.
