import os
import smtplib
import datetime as dt
import time
from random import choice
import pandas
import logging



    # with open("love_list.txt") as data:
    #     love_list = [sentence.strip() for sentence in data]

my_email = "naamaavit@gmail.com"
my_password = os.getenv('MAIL_PASS')

now = dt.datetime.now()
hour = now.hour
month = now.month
day = now.day

logging.info(now.minute)
bd_data = pandas.read_csv("data.csv")
same_day = bd_data[bd_data.day == day]
same_day_and_month = same_day[same_day.month == month]
list_of_names = same_day_and_month["name"].to_list()
list_of_emails = same_day_and_month["email"].to_list()
list_of_letters = ["first_letter.txt", "second_letter.txt"]
place = 0

print("shay-print")
logging.info('shay-info')
while True:
    time.sleep(5)
    logging.info('55555')
    logging.info(now)
    if now.hour == 18 and now.minute == 56:
        print('time to send mail')
        for name in list_of_names:
            letter_to_send = choice(list_of_letters)
            with open(letter_to_send, "r") as letter_to_send:
                new_letter = letter_to_send.read()
            send_letter = new_letter.replace("[Name]", name)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(from_addr=my_email, to_addrs=list_of_emails[place],
                                    msg=f"subject:Love Letter\n\n{send_letter}")
            place +=1
            time.sleep(20)


# better way to acess the data:
# new_dict = {(column["day"], column["month"]):(column["email"], column["name"]) for (index, column) in bd_data.iterrows()}
# print(new_dict)

# Angela solution:
# from datetime import datetime
# import pandas
# import random
# import smtplib
#
# MY_EMAIL = "YOUR EMAIL"
# MY_PASSWORD = "YOUR PASSWORD"
#
# today = datetime.now()
# today_tuple = (today.month, today.day)
#
# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])
#
#     with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"
#         )



