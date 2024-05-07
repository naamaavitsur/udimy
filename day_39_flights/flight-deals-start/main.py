import requests
import json
from config import wanted_flights, URL_KIWI, header_kiwi
from notification_manager import SendMessage

def add_user_details():
    user_first_name = input("Please enter your first name: ")
    user_second_name = input("Please enter your second name: ")
    user_email = input("Please enter your E-mail: ")
    iata_flight_from = input("please insert IATA code of the city you wanna travel from:")
    iata_flight_to = input("please insert IATA code of the city you wanna travel to:")
    maximum_money = int(input("please write maximum price you wanna pay: "))
    return user_first_name, user_second_name, user_email, iata_flight_from, iata_flight_to, maximum_money

def list_of_destination_info(iata_flight_to, iata_flight_from, max_price):
    params_kiwi = {
        'fly_from': iata_flight_from,
        'fly_to': iata_flight_to,
        'date_from': '01/05/2024',
        'date_to': '15/05/2024',
        'return_from': '04/05/2024',
        'return_to': '20/05/2024',
    }

    response = requests.get(url=URL_KIWI, headers=header_kiwi, params=params_kiwi)
    data = response.json()
    with open("data.json", 'w') as f:
        json.dump(data, f, indent=2)
    data = response.json()["data"]
    list_of_dicts = []
    for i in data:
        flight_date = i["local_departure"]
        price = int(i["price"])
        city_from = i["cityFrom"]
        city_to = i["cityTo"]
        if price <= max_price:
            dict_per_destination = {"flight_date": flight_date, "price": price, "city_from": city_from, "city_to": city_to}
            list_of_dicts.append(dict_per_destination)
    return list_of_dicts


user_first_name, user_second_name, user_email, iata_flight_from, iata_flight_to, maximum_money = add_user_details()


list = list_of_destination_info(iata_flight_to, iata_flight_from, maximum_money)
if list:
    send_message = SendMessage(list, user_first_name, user_email)
else:
    print("there is no flights for you!")
