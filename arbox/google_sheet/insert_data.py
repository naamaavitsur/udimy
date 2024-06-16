import os
import gspread
import json
from google.oauth2.service_account import Credentials
from monthly_statistic.get_arbox_data import get_token
from monthly_statistic.get_dates import get_previous_month_date, get_default_start_end_dates
from monthly_statistic.sum_monthly_data import create_stats_data_to_insert, create_class_data
from datetime import datetime
from dotenv import load_dotenv, dotenv_values
load_dotenv()


creds_file_name = "creds.json"


def insert_data_to_class(sheet, token, start_data, end_data):
    list_of_class_data = create_class_data(token, start_data, end_data)
    work_sheet = sheet.worksheet('דוח חוגים')
    print("I have the חוגים sheet you want to insert")
    column = get_column_to_insert(work_sheet)
    row = 1
    for i in list_of_class_data:
        work_sheet.update_cell(row=row, col=column, value=i)
        row += 1


def insert_data_to_statistic(sheet, token, start_date, end_date):
    work_sheet = sheet.worksheet('naama')
    print("I have the sheet you want to insert")
    column = get_column_to_insert(work_sheet)
    row = 1
    list_of_stats_data = create_stats_data_to_insert(token, start_date, end_date)
    for i in list_of_stats_data:
        work_sheet.update_cell(row=row, col=column, value=i)
        row += 1
    print(f"i did it!! i insert {row} rows")


def read_amount_of_injury_reports(sheet, start_date, end_date):
    injury_counter = 0
    work_sheet = sheet.worksheet('פצועים פצועות')
    row_num = 1
    cell_val = work_sheet.cell(row_num, 1).value
    # print(f"cell_val: {cell_val}, {row_num}")
    while cell_val:
        cell_val = work_sheet.cell(row_num, 1).value
        # print(f"cell_val: {cell_val}, {row_num}")
        row_num += 1
        try:
            val_datetime = datetime.strptime(cell_val, '%Y-%m-%d %H:%M:%S')
        except Exception as e:
            print(f"ERROR- cell val: {cell_val} in row num: {row_num} failed to convert to datetime, skip")
            print(f"ERROR- {e}")
            continue
        if start_date <= val_datetime <= end_date:
            injury_counter += 1
    return injury_counter


def get_column_to_insert(work_sheet):
    col_num = 1
    cell_val = work_sheet.cell(row=1, col=col_num).value
    while cell_val:
        col_num += 1
        cell_val = work_sheet.cell(row=1, col=col_num).value
    return col_num


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


def main(start_date, end_date):
    token = get_token()
    create_creds_json()
    sheet = sheet_connection()
    injury_count = read_amount_of_injury_reports(sheet, start_date=start_date, end_date=end_date)
    insert_data_to_statistic(sheet, token, start_date, end_date)
    insert_data_to_class(sheet, token, start_date, end_date)


if __name__ == '__main__':
    start_date, end_date = get_default_start_end_dates()
    main(start_date, end_date)
