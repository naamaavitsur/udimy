import requests
from datetime import datetime, timedelta
from twilio.rest import Client
import os

today = datetime.now()
today_format = today.strftime("%Y-%m-%-d")
yesterday_format = (today + timedelta(days=-1)).strftime("%Y-%m-%-d")
print(today_format)
print(yesterday_format)


account_sid = os.getenv("AC_SI")
auth_token = os.getenv("AU_TO")
mail = os.getenv("MAIL")
arbox_password = os.getenv("PASS")


# nano ~/.bashrc
#
# export MY_VARIABLE="my_value"
# export ANOTHER_VARIABLE="another_value"
#
# source ~/.bashrc
def get_token() -> str:
    headers = {
        'authority': 'arboxserver.arboxapp.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,he;q=0.7',
        'content-type': 'application/json',
        'lang': 'he',
        'manage': 'system',
        'origin': 'https://manage.arboxapp.com',
        'referer': 'https://manage.arboxapp.com/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    params = {
        'XDEBUG_SESSION_START': 'PHPSTORM',
    }

    json_data = {
        'email': mail,
        'password': arbox_password,
    }

    response = requests.post('https://arboxserver.arboxapp.com/api/v2/login', params=params, headers=headers, json=json_data)
    if response.status_code != 200:
        print("problem in get token:")
        print(response.status_code)
        print(response.text)
    token = response.json()["token"]
    return token


def selling_items():
    headers = {
        'authority': 'arboxserver.arboxapp.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,he;q=0.7',
        'content-type': 'application/json',
        'lang': 'he',
        'manage': 'system',
        'origin': 'https://manage.arboxapp.com',
        'referer': 'https://manage.arboxapp.com/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'token': token,
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    params = {
        'XDEBUG_SESSION_START': 'PHPSTORM',
    }

    json_data = {
        'action': None,
        'created_by_user': None,
        'from_date': yesterday_format,
        'to_date': yesterday_format,
        'location_box_id': None,
        'report_type': 'detailedReport',
        'sub_action': None,
    }

    response = requests.post(
        'https://arboxserver.arboxapp.com/api/manage/v2/reports/salesReport',
        params=params,
        headers=headers,
        json=json_data,
    )


    response = response.json()
    all_selling_items = {}
    for item in response:
        selling_product = item["membership_type_name"]
        if selling_product in all_selling_items:
            all_selling_items[selling_product] += 1
        else:
            all_selling_items[selling_product] = 1
    number_of_product = 0
    for i in all_selling_items:
        number_of_product += all_selling_items[i]

    messege = (f"{number_of_product} items were sold today: \n")
    for i in all_selling_items:
        messege += f"  *{i} ({all_selling_items[i]})\n"

    return messege


def entrence():
    headers = {
        'authority': 'arboxserver.arboxapp.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,he;q=0.7',
        'content-type': 'application/json',
        'lang': 'he',
        'manage': 'system',
        'origin': 'https://manage.arboxapp.com',
        'referer': 'https://manage.arboxapp.com/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'token': token,
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    params = {
        'XDEBUG_SESSION_START': 'PHPSTORM',
    }

    json_data = {
        'from_date': yesterday_format,
        'to_date': yesterday_format,
    }

    response = requests.post(
        'https://arboxserver.arboxapp.com/api/manage/v2/reports/entranceReport',
        params=params,
        headers=headers,
        json=json_data,
    )

    entrence_number = 0
    response = response.json()
    for i in response:
        if i["success"] == 1:
            entrence_number += 1

    return f"Today {entrence_number} people entered the gym"


def send_whatsapp():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body=today_message,
        to='whatsapp:+972547833192'
    )


token = get_token()
selling = selling_items()
entrence_today = entrence()
today_message = f"{selling}\n{entrence_today}\n\nGood night!❤️ "
print(today_message)
send_whatsapp()
print("everything went cool!")





