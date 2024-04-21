import time

import requests
from twilio.rest import Client


api_key = "8c8cca68cdacc56f8bde4fe02fb81675"
parameters = {
    "lat" : "31.768318",
    "lon" : "35.213711",
    "appid": "67ff45aa233bded1f4167bec1a04a668",
    "cnt": "4"
}


weather_respones = requests.get("https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
weather_respones.raise_for_status()
weather_data = weather_respones.json()["list"]
will_rain = False
for day in weather_data:
    weather = int(day["weather"][0]["id"])
    if weather < 700:
        will_rain = True
if will_rain:
    messege = "bring umbrella"
    print(messege)
if not will_rain:
    messege = "dont bring umbrella"
    print(messege)

account_sid = 'AC06c13f5ccf2581297b896477d328012e'
auth_token = 'e5377962b1861e267991c33f5dd4bd7e'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body= messege,
  to='whatsapp:+972547833192'
)


print(message.status)
