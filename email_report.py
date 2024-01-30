import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

def send_email():
    # Email configuration
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    receiver_email = "recipient@example.com"
    subject = "Daily Report"
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
