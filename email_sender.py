# -*- coding: utf-8 -*-
"""Email Sender.ipynb

import smtplib
from email.message import EmailMessage
import ssl
import os

email_sender = 'tuhinbdesh@gmail.com'#'noc@mos5tel.com''tuhinbdesh@gmail.com'
email_password = 'uvxn qkzh vcar xpgc'#'WPJRW1DCT0Vn'#'uvxn qkzh vcar xpgc'#os.environ.get("EMAIL_PASSWORD")
email_receiver = ['tuhinbdesh@gmail.com','noc@mos5tel.com','babul_bd2003@yahoo.com']

subject = 'Check out the message'
body = """
This for test mail
"""
em=EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject

em.set_content(body)

context = ssl.create_default_context()


with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
