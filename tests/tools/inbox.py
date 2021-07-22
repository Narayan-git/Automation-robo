import imaplib
import email

from bs4 import BeautifulSoup
from lxml import etree
# import requests

host = 'w0174d79.kasserver.com'
username = '@leadpaka.de'
password = 'vQDZKq5md99xLDef'


def get_inbox(sender_mail_id = None, subject = None):
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    #_, search_data = mail.search(None, 'TO "qwert@leadpaka.de"')
    if (subject):
        _, search_data = mail.search(None, f'TO "{sender_mail_id}" SUBJECT "{subject}"')
    else:
        _, search_data = mail.search(None,f'TO "{sender_mail_id}"')
    my_message = []
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        # print(data[0])
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        for header in ['subject', 'to', 'from', 'date']:
            #print("{}: {}".format(header, email_message[header]))
            email_data[header] = email_message[header]
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                charset = part.get_content_charset()
                body = part.get_payload(decode=True)
                email_data['body'] = body.decode(encoding=charset, errors="ignore")
            elif part.get_content_type() == "text/html":
                charset = part.get_content_charset()
                html_body = part.get_payload(decode=True)
                email_data['html_body'] = html_body.decode(encoding=charset, errors="ignore")
        my_message.append(email_data)
    return my_message[0]


def get_message_by_subject_mail(email_subject ,  email):
    # my_inbox = get_inbox()
    my_inbox = [{'subject': 'Please Verify Your Email Account', 'to': 'baap1@leadpaka.de, baap2@leadpaka.de', 'from': 'Baap SMTP <baapsmtp@gmail.com>', 'date': 'Sat, 29 May 2021 11:02:09 +0530', 'body': 'Verify Your Email Address\r\nThanks for creating an account with the verification demo app. Please\r\nfollow the link below to verify your email address\r\nhttp://localhost:8000/register/verify/NfoUVArLZVTU6DSNMrarGnYddACQHj.\r\n', 'html_body': '<div dir="ltr"><div class="gmail-gs" style="margin:0px;padding:0px 0px 20px;width:980.364px;font-family:Roboto,RobotoDraft,Helvetica,Arial,sans-serif;font-size:medium"><div class="gmail-"><div id="gmail-:nu" class="gmail-ii gmail-gt" style="font-size:0.875rem;direction:ltr;margin:8px 0px 0px;padding:0px"><div id="gmail-:nt" class="gmail-a3s gmail-aiL" style="overflow:hidden;font-variant-numeric:normal;font-variant-east-asian:normal;font-stretch:normal;font-size:small;line-height:1.5;font-family:Arial,Helvetica,sans-serif"><div><h2>Verify Your Email Address</h2><div>Thanks for creating an account with the verification demo app. Please follow the link below to verify your email address\xa0<a href="http://localhost:8000/register/verify/NfoUVArLZVTU6DSNMrarGnYddACQHj" target="_blank">http://localhost:8000/register/verify/NfoUVArLZVTU6DSNMrarGnYddACQHj</a>.<div class="gmail-yj6qo"></div><div class="gmail-adL"><br></div></div><div class="gmail-adL"></div></div><div class="gmail-adL"></div></div></div><div class="gmail-hi" style="border-bottom-left-radius:1px;border-bottom-right-radius:1px;padding:0px;width:auto;background:rgb(242,242,242);margin:0px"></div></div></div><br class="gmail-Apple-interchange-newline"></div>\r\n'}, {'subject': 'Please Verify Your Email Account', 'to': 'baap1@leadpaka.de, baap2@leadpaka.de', 'from': 
'Baap SMTP <baapsmtp@gmail.com>', 'date': 'Sat, 29 May 2021 11:02:09 +0530', 'body': 'Verify Your Email Address\r\nThanks for creating an account with the verification demo app. Please\r\nfollow the link below to verify your email address\r\nhttp://localhost:8000/register/verify/NfoUVArLZVTU6DSNMrarGnYddACQHj.\r\n', 'html_body': '<div dir="ltr"><div class="gmail-gs" style="margin:0px;padding:0px 0px 20px;width:980.364px;font-family:Roboto,RobotoDraft,Helvetica,Arial,sans-serif;font-size:medium"><div class="gmail-"><div id="gmail-:nu" class="gmail-ii gmail-gt" style="font-size:0.875rem;direction:ltr;margin:8px 0px 0px;padding:0px"><div id="gmail-:nt" class="gmail-a3s gmail-aiL" style="overflow:hidden;font-variant-numeric:normal;font-variant-east-asian:normal;font-stretch:normal;font-size:small;line-height:1.5;font-family:Arial,Helvetica,sans-serif"><div><h2>Verify Your Email Address</h2><div>Thanks for creating an account with the verification demo app. Please follow the link below to verify your email address\xa0<a href="http://localhost:8000/register/verify/NfoUVArLZVTU6DSNMrarGnYddACQHj" target="_blank">http://localhost:8000/register/verify/NfoUVArLZVTU6DSNMrarGnYddACQHj</a>.<div class="gmail-yj6qo"></div><div class="gmail-adL"><br></div></div><div class="gmail-adL"></div></div><div class="gmail-adL"></div></div></div><div class="gmail-hi" style="border-bottom-left-radius:1px;border-bottom-right-radius:1px;padding:0px;width:auto;background:rgb(242,242,242);margin:0px"></div></div></div><br class="gmail-Apple-interchange-newline"></div>\r\n'}]
    for each_mail in my_inbox:
        print(len(my_inbox))
        if(email.lower() in each_mail['to'].lower()):
            if(email_subject in each_mail['subject']):
                print(each_mail['subject'])


def html_processing(data):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(f"{data}")
    soup.find()

    soup = BeautifulSoup(data, "html.parser")
    dom = etree.HTML(str(soup))
    
    return dom.xpath('//a')[0].get("href")

def get_subject(sender_mail_id, subject = None):
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    #_, search_data = mail.search(None, 'TO "qwert@leadpaka.de"')
    if (subject):
        _, search_data = mail.search(None, f'TO "{sender_mail_id}" SUBJECT "{subject}"')
    else:
        _, search_data = mail.search(None,f'TO "{sender_mail_id}"')
    my_message = []
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        # print(data[0])
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        for header in ['subject', 'to', 'from', 'date']:
            #print("{}: {}".format(header, email_message[header]))
            email_data[header] = email_message[header]
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                charset = part.get_content_charset()
                body = part.get_payload(decode=True)
                email_data['body'] = body.decode(encoding=charset, errors="ignore")
            elif part.get_content_type() == "text/html":
                charset = part.get_content_charset()
                html_body = part.get_payload(decode=True)
                email_data['html_body'] = html_body.decode(encoding=charset, errors="ignore")
        my_message.append(email_data)
    return my_message[-1]["subject"]



def get_mail_verification_link(email_id = None, multi_flag = None,subject = None):
    # email_id = "testmail@leadpaka.de"
    subject = get_subject(email_id)

    my_inbox = get_inbox(sender_mail_id = email_id, subject = subject)

    # print(my_inbox)

    key = my_inbox["html_body"]
    # print(key)
    hrf_link = html_processing(key)
    # print(f"mail verification Link{hrf_link}")
    return hrf_link
    

# verification_link = get_mail_verification_link(email_id="testmailrabin@leadpaka.de")
# print(verification_link)

# #find subject
# subject = get_subject(sender_mail_id="testmail@leadpaka.de")
