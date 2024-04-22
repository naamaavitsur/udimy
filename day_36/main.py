import requests
from twilio.rest import Client
import os

api_active_members = "https://api.arboxapp.com/index.php/api/v2/users"
headers = {
    "apiKey": os.environ.get("APIKEY")
}
body_params = {"active": 1}
number_total = 0
number_whithout_mail = 0

response = requests.get(api_active_members, headers=headers, params=body_params)
response.raise_for_status()
response_jason= response.json()

for i in response_jason:
    mail= i['email']
    number_total += 1
    if mail == None :
        number_whithout_mail += 1
print("have all the data")

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_="whatsapp:+14155238886",
  body=f" monkeys have: {number_total} active claient and {number_whithout_mail} of them without mail. please pay attention",
  to='whatsapp:+972547833192'
)
print(message.status)
print("i send whatsupp")