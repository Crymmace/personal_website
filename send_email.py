import os
import smtplib
import ssl
from dotenv import load_dotenv

load_dotenv()


def send_email(message):

    host = "smtp.office365.com"
    port = 587

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    receiver = os.getenv("USERNAME")
    context = ssl.create_default_context()

    with smtplib.SMTP(host, port) as server:
        server.starttls(context=context)
        server.ehlo()
        server.login(username, password)
        server.sendmail(username, receiver, message)
