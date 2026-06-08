from twilio.rest import Client
from datetime import datetime
import time
import os

# Load Twilio credentials from environment variables
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
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
