import os
import gspread
import json
from google.oauth2.service_account import Credentials
from arbox.monthly_statistic.get_dates import previous_month, last_month_year
from arbox.monthly_statistic.sum_monthly_data import list_of_sum_data, list_of_class_data
print("I have all the data from arbox!")
from datetime import datetime


creds_file_name = "creds.json"

def insert_data_to_class(sheet):
    work_sheet = sheet.worksheet('דוח חוגים')
    print("I have the חוגים sheet you want to insert")
    column = get_column_to_insert(work_sheet)
    month = datetime.now().month
    row = 1
    for i in list_of_class_data:
        work_sheet.update_cell(row=row, col=column, value=i)
        row += 1


def insert_data_to_statistic(sheet):
    work_sheet = sheet.worksheet('naama')
    print("I have the sheet you want to insert")
    column = get_column_to_insert(work_sheet)
    row = 1
    for i in list_of_sum_data:
        work_sheet.update_cell(row=row, col=column, value=i)
        row += 1
    print("i did it!!")


def read_amount_of_injury_reports(sheet):
    injury_counter = 0
    work_sheet = sheet.worksheet('פצועים פצועות')
    for i in range(1,100000):
        val = work_sheet.cell(i, 1).value
        if val == None:
            break
        else:
            val_datetime = datetime.strptime(val, '%Y-%m-%d %H:%M:%S')
            month = val_datetime.month
            year = val_datetime.year
            if month == previous_month[-1] and year == last_month_year:
                injury_counter += 1
    list_of_sum_data.append(injury_counter)


def get_column_to_insert(work_sheet):
    for number in range(1, 10000000000):
        val = work_sheet.cell(row=1, col=number).value
        if val == None:
            return number


def create_creds_json():
    creds_data = {
        "type": "service_account",
        "project_id": "shay-naama",
        "private_key_id": os.getenv('SHEET_PRIVATE_KEY_ID'),
        "private_key": os.getenv('SHEET_PRIVATE_KEY').replace("\\n", "\n"),
        "client_email": os.getenv('SHEET_CLIENT_EMAIL'),
        "client_id": os.getenv('SHEET_CLIENT_ID'),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": os.getenv('SHEET_CLIENT_X509'),
        "universe_domain": "googleapis.com"
    }
    with open(creds_file_name, 'w') as f:
        json.dump(creds_data, f)


def sheet_connection():
    scope = [
        "https://www.googleapis.com/auth/spreadsheets"
    ]
    creds = Credentials.from_service_account_file(creds_file_name, scopes=scope)
    client = gspread.authorize(creds)
    sheet_id = "12mIx8jTPaC5OzABlIL1j4OJf823GRr3Nb2WzY8jwvDk"
    sheet = client.open_by_key(sheet_id)
    return sheet


def main():
    create_creds_json()
    sheet = sheet_connection()
    read_amount_of_injury_reports(sheet)
    insert_data_to_statistic(sheet)
    insert_data_to_class(sheet)


if __name__ == '__main__':
    create_creds_json()
    sheet = sheet_connection()
    read_amount_of_injury_reports(sheet)
    insert_data_to_statistic(sheet)
    insert_data_to_class(sheet)






