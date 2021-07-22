import imaplib
import pprint
import email
from email.header import decode_header
import webbrowser
import os


imap_host = 'imap.gmail.com'
imap_user = 'softlezy@gmail.com'
imap_pass = 'Rabin650@'
def clean(text):
    # clean text for creating a folder
    return "".join(c if c.isalnum() else "_" for c in text)

# connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host)

## login to server
imap.login(imap_user, imap_pass)

status , messages = imap.select('INBOX')
result, data = imap.search(None, '(FROM "Marktplatz Mittelstand")')
ids = data[0]
id_list = ids.split()
latest_email = id_list[-1]
result, data= imap.fetch(latest_email, "(RFC822)")
raw_email = data[0][1]
print(raw_email)
# close the connection and logout
imap.close()
imap.logout()