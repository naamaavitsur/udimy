from twilio.rest import Client
import os
import smtplib

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
my_password = os.getenv('GMAIL_PASS')


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
            self.body += f"From: {self.city_from} at {date}, {hour} to {self.destination}. price:{self.price}\n"
            self.send_mail(mail)


    def send_whatsupp(self):
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body= self.body,
            to='whatsapp:+972547833192'
        )

    def send_mail(self, email):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="naamaavit@gmail.com", password=my_password)
            connection.sendmail(from_addr="naamaavit@gmail.com", to_addrs=email,
                                msg=f"subject:Flights!\n\n{self.body}")
