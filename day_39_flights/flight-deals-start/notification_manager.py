from twilio.rest import Client
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
my_password = os.getenv('GMAIL_PASS')
my_email = "naamaavit@gmail.com"


class SendMessage:
    def __init__(self, list, name, mail):
        self.list = list
        self.body = f"hey {name},\nThis is the flights i find for you:\n"
        for dict in list:
            self.date = dict["flight_date"]
            self.price = dict["price"]
            self.destination = dict["city_to"]
            self.city_from = dict["city_from"]
            date = self.date[:10]
            hour = self.date[11:16]
            self.body += f"From: {self.city_from} at {date}, {hour} \nTo: {self.destination}. \nprice: {self.price}\n\n"
        # self.send_mail(mail)
        self.send_whatsupp()


    def send_whatsupp(self):
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body= self.body,
            to='whatsapp:+972547833192'
        )

    def send_mail(self, email):
        msg = MIMEMultipart()
        msg['Subject'] = "Flights!"
        msg.attach(MIMEText(self.body, 'plain', 'utf-8'))

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=msg.as_string())



