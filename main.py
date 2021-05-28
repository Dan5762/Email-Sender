import json
import time
import yagmail
import smtplib
from random_word import RandomWords

with open('secrets.json', 'r') as f:
    secrets = json.load(f)

def get_contacts():
    with open('contacts.csv') as f:
        contacts = f.readlines()

    contacts = [contact.replace('\n', '') for contact in contacts]

    return contacts

def send_emails(recipients):
    server = yagmail.SMTP(secrets['email'], secrets['password'])

    subject = 'testing'

    r = RandomWords()

    for idx in range(1000):
        random_word = r.get_random_word()
        while type(random_word) is not str:
            random_word = r.get_random_word()

        content = 'hello there ' + random_word
        print(f"Sent: {idx}", end ="\r")
        try:
            server.send(to=recipients[0], subject=subject, contents=content)
        except smtplib.SMTPServerDisconnected:
            print(f"Sent: {idx}, Sleeping", end ="\r")
            time.sleep(60)
            server.send(to=recipients[0], subject=subject, contents=content)

        if idx % 100 == 0:
            print(f"Sent: {idx}, Sleeping", end ="\r")
            time.sleep(120)

if __name__ == "__main__":
    contacts = get_contacts()

    send_emails(['Danlong1998@icloud.com'])
