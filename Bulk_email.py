#!/usr/bin/env python3

import smtplib
from email.message import EmailMessage
import ssl
import csv

user = 'pablos.com'
passwords = 'passwords'

def read_emails():
    contacts = []
    with open('emailDemo.csv', 'r') as emails:
        read_em = csv.DictReader(emails)
        for line in read_em:
            contacts.append({'First_Name': line['First_Name'], 'Email': line['Email']})
    return contacts

user = "pablo.com"
passwords = 'ore4'

def send_message():
    subject = 'Personalizing email with python script'
    contacts = read_emails()
    context = ssl.create_default_context()

    for contact in contacts:
        name = contact['First_Name']
        email = contact['Email']
        body = f"""
        Hey {name},

        I hope you are doing great. A friend of mine had a problem creating a python script that could help send out an email to his fellow employees.
        However, he came across my LinkedIn profile and found out that I have skills in python. I was then hired to help him.

        I am sending you this script to test if it is really working.

        Warm regards,
        Alimasi (Kit)
        """
        
        msg = EmailMessage()
        msg['From'] = user
        msg['To'] = email
        msg['Subject'] = subject
        msg.set_content(body)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(user, passwords)
            smtp.send_message(msg)
            print(f'Email sent to {name}')

send_message()