import requests
from datetime import datetime, timedelta
from twilio.rest import Client
import os
import config
import json

send_message_to = {"ilai": "+972527808418", "oren":"+972502239911",
"shahar":"+972522492230", "naama": "+972547833192"}



apiKey = os.getenv("JF_API")
formID = "231333863831051"
whatsapp_token = os.getenv("WHATSAPP_TOKEN")
account_sid = os.getenv("AC_SI")
auth_token = os.getenv("AU_TO")
mail = os.getenv("MAIL")
arbox_password = os.getenv("PASS")
whatsapp_token_permenent = os.getenv("FACBOOK_TOKEN_PERMENENT")

today = datetime.now()
today_format = today.strftime("%Y-%m-%-d")
yesterday_format = (today + timedelta(days=-1)).strftime("%Y-%m-%-d")


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


def get_selling_items():
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
    return response


def get_number_of_injuries():
    response = requests.get(f"https://api.jotform.com/form/{formID}/submissions?apiKey={apiKey}")
    data = response.json()["content"]
    count = 0
    for submission in data:
        date_happened = submission["created_at"][0:10]
        if date_happened == yesterday_format:
            count += 1
    return count


# def number_of_selled_item(selled_items):
#     all_selling_items = {}
#     for item in response:
#         selling_product = item["membership_type_name"]
#         if selling_product in all_selling_items:
#             all_selling_items[selling_product] += 1
#         else:
#             all_selling_items[selling_product] = 1
#     number_of_product = 0
#     for i in all_selling_items:
#         number_of_product += all_selling_items[i]
#
#     messege = (f"{number_of_product} items were sold today: \n")
#     for i in all_selling_items:
#         messege += f"  *{i} ({all_selling_items[i]})\n"
#         return messege


def get_selling_profit(list_of_selling_items):
    money_paid = 0
    for item in list_of_selling_items:
        money_paid += item["paid"]
    return money_paid


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


def get_all_active_user(token):
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
        'reportType': 'detailedReport',
        'locationBox': None,
    }

    response = requests.post(
        'https://arboxserver.arboxapp.com/api/manage/v2/reports/activeMembershipsReport',
        params=params,
        headers=headers,
        json=json_data,
    )

    return response.json()


def count_member_type(active_member:dict, membership_type:list) -> int:
    membership_count = 0
    for client in active_member:
        if client["membership_type"] in membership_type:
            membership_count += 1
    return membership_count


def get_amount_of_spesific_item(wanted_item, selling_list):
    count = 0
    for item in selling_list:
        if item["membership_type_name"] == wanted_item:
            count += 1
    return count


def number_of_child_in_class(members_list):
    classes_count = 0
    for client in active_members:
        if client["department_name"] == "חוגים":
            if client["membership_type"] != "חוג עובדים":
                classes_count += 1
    return classes_count


def get_new_client(token):

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
        'dateOf': None,
        'filterDatesBy': 'signedDate',
        'formType': 'MEDICALCERT',
        'fromDateFilter': yesterday_format,
        'toDateFilter': yesterday_format,
        'location': None,
        'userType': 'members',
    }

    response = requests.post(
        'https://arboxserver.arboxapp.com/api/manage/v2/reports/signedFormsReport',
        params=params,
        headers=headers,
        json=json_data,
    )

    response = response.json()

    count_new_client = 0
    for i in response:
        if i["name"] == "טופס אישור השתתפות":
            count_new_client += 1
    return count_new_client


def send_whatsapp(message, people):
    url = 'https://graph.facebook.com/v20.0/317183528149149/messages'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {whatsapp_token_permenent}'
    }

    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": people,
        "type": "text",
        "text": {
            "preview_url": True,
            "body": message
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("Success!")
        print(response.json())
    else:
        print(f"Failed with status code: {response.status_code}")
        print(response.text)


token = get_token()
active_members = get_all_active_user(token)
monthly_members_count = count_member_type(active_members, config.all_renewable)
list_of_selling_items = get_selling_items()
money_paid = get_selling_profit(list_of_selling_items)
introduction_card = get_amount_of_spesific_item("כרטיסיית הכרות + צ'יפ", list_of_selling_items)
basics_workshop = get_amount_of_spesific_item("סדנת יסודות", list_of_selling_items)
class_kids = number_of_child_in_class(active_members)
new_client = get_new_client(token)
number_of_injuries = get_number_of_injuries()
message = (f"עדכון יומי:🦧\n"
           f"{yesterday_format}\n"
           f"מספר מנויים: {monthly_members_count}\n"
           f"סהכ מכירות אתמול : {money_paid}\n"
           f"מכירות כרטיסיית היכרות: {introduction_card}\n"
           f"מכירות סדנת יסודות: {basics_workshop}\n"
           f"ילדי חוגים: {class_kids}\n"
           f"לקוחות חדשים: {new_client}\n"
           f"דיווחי פציעה: {number_of_injuries}\n")
for people in send_message_to.values():
    send_whatsapp(message, people)






