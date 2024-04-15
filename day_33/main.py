import time

import requests
from datetime import datetime
from config import MAX_LNG, MIN_LNG, MAX_LAT, MIN_LAT, MY_LNG, MY_LAT
import os
import smtplib


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

my_email = "naamaavit@gmail.com"
my_password = os.getenv('MAIL_PASS')


def is_above_me(MAX_LNG, MIN_LNG, MAX_LAT, MIN_LAT, iss_latitude, iss_longitude):
    if MIN_LAT < iss_latitude < MAX_LAT and MAX_LNG > iss_longitude > MIN_LNG:
        return True
    else:
        return False


def is_dark(sunrise, sunset):
    time_now = datetime.now()
    hour = time_now.hour
    if not sunrise < hour < sunset:
        return True
    else:
        return False


def send_mail(my_email, my_password):
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg=f"subject:the iss is above you!\n\nhave a look\n Love,\nNaama")
            print("an email send")
    except Exception as e:
        print(f"cannot conect to the email\n{e}")
        exit(1)


def get_iss_location():
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()
        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])
        print(f"the iss location is: latituse:{iss_latitude},longitude: {iss_longitude}")
        return iss_latitude, iss_longitude

    except Exception as e:
        print(f"cannot get iss location\n {e}")
        exit(1)


def get_sun_hours(parameters):
    try:
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        if not data.get('results'):
            print(f"there is no 'results' in the response: {response.text}")
            exit(1)
        if not data['results'].get('sunset'):
            print(f"there is no 'sunrise' in the response: {response.text}")
            exit(1)
        if not data['results'].get('sunrise'):
            print(f"there is no 'sunset' in the response: {response.text}")
            exit(1)
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
        return sunrise, sunset
    except Exception as b:
        print(f"cannot do response for sunset and sunrise\n{b}")
        exit(1)


send_mail(my_email, my_password)

while True:
    time.sleep(60)
    iss_latitude, iss_longitude = get_iss_location()
    sunrise, sunset = get_sun_hours(parameters)
    if is_above_me(MAX_LNG, MIN_LNG, MAX_LAT, MIN_LAT, iss_latitude, iss_longitude) and is_dark(sunrise, sunset):
        send_mail(my_email, my_password)
    else:
        print("you cannot see the iss now. lets check in one min")


