import requests
import os
from datetime import datetime


headers = {"apiKey": os.getenv("API_KEY")}
try_date = "1990-03-05"
date_object = datetime.strptime(try_date, '%Y-%m-%d')
print(type(date_object))

def check_if_mail_exist(mail:str):
    mail_response = requests.get(url="https://api.arboxapp.com/index.php/api/v2/searchUser",headers=headers, params= {"user": mail})
    print(mail_response.json())
    add_number = 1
    while mail_response.json()[0].get("statusCode") != 200:
        print("there is user with this mail")
        if "gmail" in mail:
            new_mail = add_number_to_mail(mail, add_number)
            add_number += 1
            mail_response = requests.get(url="https://api.arboxapp.com/index.php/api/v2/searchUser",
                                         headers=headers,
                                         params={"user": new_mail})
            print(mail_response.json())
    print(f"this mail: {new_mail}, is not exict. now i will make it ")
    #TODO why its 200??
    # creat_user()


def add_number_to_mail(mail, number):
    local_part, domain = mail.split('@')
    new_mail = local_part + f"+{number}" + domain
    return new_mail


def create_user(first_name, last_name, email, phone, id, birthday, gender=None, sms=None):
    create_user_url = "https://api.arboxapp.com/index.php/api/v2/user"
    params = {"first_name": first_name,
              "last_name": last_name,
              "email": email,
              "active": 0 ,
              "phone" : phone,
              "gender": gender,
              "personal_id": id,
              "birthday": birthday,#datetime object
              "allow_sms": sms

              }

    response = requests.post(url=create_user_url, headers=headers, params=params)


def get_user_fk(user_id):
    response = requests.get(url=f"https://api.arboxapp.com/index.php/api/v2/user/{user_id}", headers=headers)
    print(response.json())
    user_fk = response.json()['data']['user_fk']
    return user_fk

if __name__ == '__main__':
    # check_if_mail_exist("naamaavit@gmail.com")
    print(get_user_fk(862904))
