#!/usr/bin/env python3

import smtplib
import getpass
from email.message import EmailMessage
from smtplib import SMTPException

def email_server():
    # Email sender and recipient details
    sender = "pabloalimasi233@gmail.com"
    sender_name = 'Bill Gates'
    
    # Prompt user for the receiver's name
    receiver_name = input('Enter the recipient\'s name: ').strip()
    recipient = input('Enter the recipient\'s email: ')

    # Prepare email message
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = 'Greetings from {} to {}!'.format(sender_name, receiver_name)

    # Split name to personalize message
    first_name = receiver_name.split(' ', 1)[0]

    # Email body
    body = f"""Hey {first_name}!

I hope this email finds you well.
This is to let you know that my firstborn is getting married this Sunday,
and I don't want you to miss it.

Best regards,
{sender_name}"""
    message.set_content(body)

    mail_pass = getpass.getpass('Enter your email password: ')

    try:
        # Create a connection to the mail server
        with smtplib.SMTP("smtp.gmail.com", 587) as mail_server:
            mail_server.set_debuglevel(1)  # To see communication between client/server
            mail_server.starttls()  # Secure the connection
            mail_server.login(sender, mail_pass)  # Log in

            # Send the email
            mail_server.send_message(message)
            print('Email sent successfully!')
    except SMTPException as e:
        print(f'Failed to send email: {e}')
    except Exception as ex:
        print(f'An error occurred: {ex}')

if __name__ == "__main__":
    email_server()
