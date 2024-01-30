import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
import datetime
from dotenv import load_dotenv

# Load the dotenv file
load_dotenv()

# Get email configuration from environment variables
sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")
receiver_email = os.getenv("RECEIVER_EMAIL")
subject = os.getenv("EMAIL_SUBJECT", f"Daily Report {now}")
body = os.getenv("EMAIL_BODY", "This is your daily report.")

# get the current date and time
now = datetime.datetime.now()

def send_email(sender_email, sender_password, receiver_email, subject=None, body=None):
    if subject is None:
        subject = f"Daily Report {now}"
    if body is None:
        body = "This is your daily report."

    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Connect to SMTP server
    with smtplib.SMTP_SSL("smtp.example.com", 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

# Schedule the email to be sent daily at a specific time (e.g., 9:00 AM)
schedule.every().day.at("09:00").do(send_email)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
