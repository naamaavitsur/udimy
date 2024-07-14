import logging
import requests
from datetime import datetime, timedelta
import os
import config
import json

send_message_to = {
    # "ilai": "+972527808418",
    # "oren":"+972502239911",
    # "shahar":"+972522492230",
     "naama": "+972547833192"
                   }



apiKey = os.getenv("JF_API")
formID = "231333863831051"
whatsapp_token = os.getenv("WHATSAPP_TOKEN")
account_sid = os.getenv("AC_SI")
auth_token = os.getenv("AU_TO")
mail = os.getenv("MAIL")
arbox_password = os.getenv("PASS")
whatsapp_token_permenent = os.getenv("FACBOOK_TOKEN_PERMENENT")

today = datetime.now()
today_format = today.strftime("%Y-%m-%d")
yesterday = today - timedelta(days=1)
yesterday_month = yesterday.month
yesterday_year = yesterday.year
yesterday_format = yesterday.strftime("%Y-%m-%d")
message_date_formate =  yesterday.strftime("%d.%m.%Y")


def get_total_profit(token):
    try:
        headers = {
            'authority': 'api.arboxapp.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,he;q=0.7',
            'accesstoken': token,
            'boxfk': '845',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://angularmanage.arboxapp.com',
            'referer': 'https://angularmanage.arboxapp.com/',
            'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        }
        json_data = {
            'init': True,
            'income_type_payment': 3,
            'submitting': True,
            'location_box': None,
            'selected_year': yesterday_year,
            'selected_month': str(yesterday_month),
            'radio_selection': 'betweenDates',
            'selectedTabb': 4,
            'from_date': yesterday_format,
            'to_date': yesterday_format,

        }

        response = requests.post('https://api.arboxapp.com/index.php/api/v1/finance/getInfoByDates/', headers=headers, json=json_data)
        response = response.json()

        total_amount = response["total_amount"]
    except:
        logging.error("Cant get total profit")
        total_amount = "המידע לא זמין"
    return total_amount


def get_token() -> str:
    try:
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
    except:
        logging.error("Cant get token")
        token = None
    return token


def get_selling_items(token):
    try:
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
    except:
        logging.error("Cant get selling items")
        response = None
    return response


def get_number_of_injuries():
    try:
        response = requests.get(f"https://api.jotform.com/form/{formID}/submissions?apiKey={apiKey}")
        data = response.json()["content"]
        count = 0
        for submission in data:
            date_happened = submission["created_at"][0:10]
            if date_happened == yesterday_format:
                count += 1
    except:
        logging.error("Cant get number of injuries")
        count = "המידע לא זמין"
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



def entrence(token):
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
    try:
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
    except:
        logging.error("Cant get active user")
        return None


def count_member_type(active_member:dict, membership_type:list) -> int:
    try:
        membership_count = 0
        for client in active_member:
            if client["membership_type"] in membership_type:
                membership_count += 1
    except:
        logging.error("Cant count member type")
        membership_count = "המידע לא זמין"
    return membership_count


def get_amount_of_spesific_item(wanted_item, selling_list):
    try:
        count = 0
        for item in selling_list:
            if item["membership_type_name"] == wanted_item:
                count += 1
    except:
        count = "המידע לא זמין"
        logging.error(f"Cant get amount of: {wanted_item}")
    return count


def number_of_child_in_class(active_members):
    try:
        classes_count = 0
        for client in active_members:
            if client["department_name"] == "חוגים":
                if client["membership_type"] != "חוג עובדים":
                    classes_count += 1
    except:
        logging.error("Cant count number of child in class")
        classes_count = "אין מידע"
    return classes_count


def get_new_client(token):
    try:

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
    except:
        count_new_client = "המידע לא זמין"
    return count_new_client


def send_whatsapp(people ,monthly_members_count, money_paid, introduction_card,basics_workshop, class_kids, new_client, number_of_injuries ):
    url = 'https://graph.facebook.com/v20.0/317183528149149/messages'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {whatsapp_token_permenent}'
    }

    data = {
        "messaging_product": "whatsapp",
        "to": people,
        "type": "template",
        "template": {
            "name": "order_message",
            "language": {
                "code": "en"
            },
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {"type": "text", "text": monthly_members_count},
                        {"type": "text", "text": money_paid},
                        {"type": "text", "text": introduction_card},
                        {"type": "text", "text": basics_workshop},
                        {"type": "text", "text": class_kids},
                        {"type": "text", "text": new_client},
                        {"type": "text", "text": number_of_injuries},
                        {"type": "text", "text": message_date_formate}
                    ]
                }
            ]
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        logging.info(f"Success response: {response.json()}")
    else:
        logging.error(f"Failed with status code: {response.status_code}")
        logging.error(f"text: {response.json()}")

def main():
    token = get_token()
    active_members = get_all_active_user(token)
    monthly_members_count = count_member_type(active_members, config.all_renewable)
    list_of_selling_items = get_selling_items(token)
    money_paid = get_total_profit(token)
    introduction_card = get_amount_of_spesific_item("כרטיסיית הכרות + צ'יפ", list_of_selling_items)
    basics_workshop = get_amount_of_spesific_item("סדנת יסודות", list_of_selling_items)
    class_kids = number_of_child_in_class(active_members)
    new_client = get_new_client(token)
    number_of_injuries = get_number_of_injuries()
    for people in send_message_to.values():
        send_whatsapp(people ,monthly_members_count, money_paid, introduction_card,basics_workshop, class_kids, new_client, number_of_injuries)
# message = (f"עדכון יומי:🦧\n"
#            f"{yesterday_format}\n"
#            f"מספר מנויים: {monthly_members_count}\n"
#            f"סהכ מכירות אתמול : {money_paid}\n"
#            f"מכירות כרטיסיית היכרות: {introduction_card}\n"
#            f"מכירות סדנת יסודות: {basics_workshop}\n"
#            f"ילדי חוגים: {class_kids}\n"
#            f"לקוחות חדשים: {new_client}\n"
#            f"דיווחי פציעה: {number_of_injuries}\n")


if __name__ == '__main__':
    main()







