import os

from twilio.rest import Client
from datetime import datetime
import time

# Twilio credentials
# Replace with your actual Account SID
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
# Replace with your actual Auth Token
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)


def send_whatsapp_message(recipient_number, message_body):
    try:
        client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to='whatsapp:' + recipient_number
        )
        print(f"Message sent successfully to {recipient_number}")
    except Exception as e:
        print(f"Failed to send message to {recipient_number}: {str(e)}")


# User inputs
name = input("Enter the recipient's name: ")
recipient_number = input(
    "Enter the recipient's WhatsApp number (with country code): ")
message_body = input("Enter the message you want to send: ")
date_str = input(
    "Enter the date and time to send the message (YYYY-MM-DD HH:MM): ")

# Scheduling logic
scheduled_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
current_time = datetime.now()
time_difference = (scheduled_time - current_time).total_seconds()

if time_difference <= 0:
    print("Scheduled time is in the past. Please enter a future time.")
else:
    print(f"Message will be sent to {recipient_number} at {scheduled_time}")
    time.sleep(time_difference)
    send_whatsapp_message(recipient_number, message_body)
