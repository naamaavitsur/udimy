import requests
import os
from datetime import datetime, timedelta

currnt_date = datetime.now()
currnt_day = currnt_date.day
current_year = currnt_date.year
befor_week = currnt_date + timedelta(days=-6)
befor_week_year = befor_week.year
befor_week_day = befor_week.day


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


def get_cancelation(token):
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
        'fromDate': '2024-04-01',
        'toDate': '2024-04-30',
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


def cancellation_fee(token):
    today_date = datetime.now().strftime("%Y-%m-01")
    this_month = (datetime.now().month)
    previos_month = str(this_month - 1)
    this_month_str = str(this_month)
    start_month = today_date.replace(this_month_str, previos_month)
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
        'from_date': start_month,
        'to_date': today_date,
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


def get_schedule_data(token):
    three_letter_current_weekday = currnt_date.strftime("%a")
    three_letter_befor_week_weekday = befor_week.strftime("%a")
    three_letter_current_month = currnt_date.strftime("%b")
    three_letter_befor_week_month = befor_week.strftime("%b")
    from_date = f"{three_letter_befor_week_weekday} {three_letter_befor_week_month} {befor_week_day} {befor_week_year}"
    to_date = f"{three_letter_current_weekday} {three_letter_current_month} {currnt_day} {current_year}"
    print(to_date, from_date)
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
        'to': f'{to_date} 00:00:00 GMT+0300',
        'from': f'{from_date} 00:00:00 GMT+0300',
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
    registering_adult_classes = 0
    kids_registering = 0
    all_registering = 0
    all_empty_place = 0
    all_max_user = 0
    number_of_under_50_percent = 0
    working_class = 0

    for i in response:
        name = i["box_categories"]["name"]
        registered = int(i["registered"])
        max_users = int(i["max_users"])
        if registered != 0 and name != "חוג עובדים":
            all_registering += registered
            all_max_user += max_users
            if registered / max_users <= 0.5:
                number_of_under_50_percent += 1
            if "בוגרים" in name:
                registering_adult_classes += registered
            else:
                kids_registering += registered
                empty_place = max_users - registered
                all_empty_place += empty_place
        else:
            working_class += registered

    occupancy_percentage = all_registering / all_max_user
    list_of_class_data = [datetime.now().strftime("%Y-%m"), working_class, registering_adult_classes,kids_registering, all_empty_place,all_max_user, round(occupancy_percentage, 2), number_of_under_50_percent]
    return list_of_class_data



if __name__ == '__main__':
    token=get_token()
    get_schedule_data(token)

