import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_email(receiver_email, subject, body):

    sender_email = os.getenv("EMAIL_ADDRESS")
    app_password = os.getenv("EMAIL_APP_PASSWORD")

    msg = EmailMessage()

    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

    return True