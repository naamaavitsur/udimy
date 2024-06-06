import requests
import os
from datetime import datetime, timedelta
import calendar

import config
# from monthly_statistic.get_dates import formated_last_day_of_month, formated_first_day_of_month, last_day_dats_with_letters, last_seven_day_dats_with_letters, last_day_datetime_formate
from config import three_letter_format, sheet_format
from monthly_statistic.get_dates import make_date_formated, get_start_and_end_for_last_week_of_last_month, get_default_start_end_dates


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
        'email': os.getenv("MAIL"),
        'password': os.getenv("PASS"),
    }

    response = requests.post('https://arboxserver.arboxapp.com/api/v2/login', params=params, headers=headers, json=json_data)
    if response.status_code != 200:
        print("problem in get token:")
        print(response.status_code)
        print(response.text)
    token = response.json()["token"]
    return token


def get_active_user(token) -> dict:
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


def count_member_type(active_member:dict, member_type:str) -> int:
    return_count = 0
    for i in active_member:
        if i["membership_type"] == member_type:
            return_count += 1
    return return_count


def get_cancelation(token, previous_month_begining, previous_month_end):
    first_day = make_date_formated(previous_month_begining, config.basic_format)
    last_day = make_date_formated(previous_month_end, config.basic_format)

    headers = {
        'authority': 'arboxserver.arboxapp.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en;q=0.9',
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
        'fromDate': first_day,
        'toDate': last_day,
        'locationId': None,
        'searchBy': 'cancelledDate',
    }

    response = requests.post(
        'https://arboxserver.arboxapp.com/api/manage/v2/reports/canceledMembershipsReport',
        params=params,
        headers=headers,
        json=json_data,
    )
    number_of_cancilation = 0
    for i in response.json():
        if i["department_name"] == "מנויים":
            number_of_cancilation +=1
    return number_of_cancilation


def cancellation_fee(token, previous_month_begining, previous_month_end):
    first_day = make_date_formated(previous_month_begining, config.basic_format)
    last_day = make_date_formated(previous_month_end, config.basic_format)
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
        'from_date': first_day,
        'to_date': last_day,
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
    number_of_cancellation_fee = 0
    for item in response.json():
        if item["membership_type_name"] == "דמי ביטול מנוי הוק":
            number_of_cancellation_fee += 1
    return number_of_cancellation_fee


def get_last_week_response(token):
    start_week, end_week = get_start_and_end_for_last_week_of_last_month()
    start_week_format = make_date_formated(start_week, three_letter_format)
    end_week_format = make_date_formated(end_week, three_letter_format)

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
        'token': token ,
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    params = {
        'XDEBUG_SESSION_START': 'PHPSTORM',
    }

    json_data = {
        'to': f'{end_week_format} 00:00:00 GMT+0300',
        'from': f'{start_week_format} 00:00:00 GMT+0300',
        'locations_box_id': 1159,
        'coachId': None,
        'hasSpace': False,
    }

    response = requests.post(
        'https://arboxserver.arboxapp.com/api/manage/v2/schedule/getScheduleBetweenDates',
        params=params,
        headers=headers,
        json=json_data,
    )

    response = response.json()["data"]
    return response


def get_last_week_data(token):
    response = get_last_week_response(token)
    registering_adult_classes = 0
    kids_registering = 0
    all_registering = 0    # all the class participent accept special
    all_empty_place = 0
    all_max_user = 0    # total place in class
    number_of_class_under_50_percent = 0
    working_class = 0

    for class_data in response:
        class_name = class_data["box_categories"]["name"]
        registered = int(class_data["registered"])
        max_users = int(class_data["max_users"])
        if registered != 0:
            if class_name not in config.list_of_exclude_class:
                all_registering += registered
                all_max_user += max_users
                if registered / max_users <= 0.5:
                    number_of_class_under_50_percent += 1
                if "בוגרים" in class_name:
                    registering_adult_classes += registered
                else:
                    kids_registering += registered
                empty_place = max_users - registered
                all_empty_place += empty_place
            else:
                working_class += registered

    occupancy_percentage = all_registering / all_max_user
    previous_month_begining = get_default_start_end_dates()[0]
    date = make_date_formated(previous_month_begining, sheet_format)
    list_of_class_data = [date, working_class, registering_adult_classes,kids_registering, all_empty_place,all_max_user, round(occupancy_percentage, 2), number_of_class_under_50_percent]
    return list_of_class_data



if __name__ == '__main__':
    token=get_token()
    get_last_week_data(token)

