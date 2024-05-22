import requests
import os


def get_token() -> str:
    headers = {
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'manage': 'system',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'lang': 'he',
        'Referer': 'https://manage.arboxapp.com/',
        'sec-ch-ua-platform': '"Linux"',
    }

    params = {
        'XDEBUG_SESSION_START': 'PHPSTORM',
    }

    json_data = {
        'email': os.getenv("MAIL"),
        'password': os.getenv("PASSWORD"),
    }



    response = requests.post('https://arboxserver.arboxapp.com/api/v2/login', params=params, headers=headers, json=json_data)
    if response.status_code != 200:
        print("problem in get token:")
        print(response.status_code)
        print(response.text)
    # print(response.json())
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


if __name__ == '__main__':
    token = get_token()
    get_cancelation(token)
