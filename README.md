# automatic_advertising
A project that scrapes business' on yellow pages, feeds the business data dynamically through a custom generated demo website, which is then automatically fed through mailgun and sent out to the scraped business'.

**config.py** - Mailgun config data for sending emails

**emailText.py** - Email content to be sent, sorted by different factors such as location, if they have a website or not, etc.

**main.py** - The main bulk of the program. Setting up database, fetching business data and storing into database.

**send_emails.py** - Fetching data from database and processing it, dynamically feeding it into the demo website. calling `python send_emails.py` will execute the program, sending the desired amount of emails as set in the code.
