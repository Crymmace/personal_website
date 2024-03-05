import os
import smtplib
import ssl
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

msg = EmailMessage()


def send_email(subject, message):

    host = "smtp.office365.com"
    port = 587

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    context = ssl.create_default_context()

    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = username
    msg['To'] = username

    with smtplib.SMTP(host, port) as server:
        server.starttls(context=context)
        server.ehlo()
        server.login(username, password)
        server.send_message(msg)
        del msg['Subject']
        del msg['From']
        del msg['To']
