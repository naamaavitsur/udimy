import gspread
from google.oauth2.service_account import Credentials
from arbox.monthly_statistic.sum_monthly_data import list_of_sum_data, list_of_class_data
print("I have all the data from arbox!")
from datetime import datetime


def insert_data_to_class():
    work_sheet = sheet.worksheet('דוח חוגים')
    print("I have the חוגים sheet you want to insert")
    column = get_column_to_insert(work_sheet)
    month = datetime.now().month
    row = 1
    for i in list_of_class_data:
        work_sheet.update_cell(row=row, col=column, value=i)
        row += 1


def insert_data_to_statistic():
    work_sheet = sheet.worksheet('naama')
    print("I have the sheet you want to insert")
    column = get_column_to_insert(work_sheet)
    month = datetime.now().month
    row = 1
    for i in list_of_sum_data:
        work_sheet.update_cell(row=row, col=column, value=i)
        row += 1
    print("i did it!!")


def read_amount_of_injury_reports():
    injury_counter = 0
    now_month = datetime.now().month
    now_year = datetime.now().year
    work_sheet = sheet.worksheet('פצועים פצועות')
    for i in range(1,100000):
        val = work_sheet.cell(i, 1).value
        if val == None:
            break
        else:
            val_datetime = datetime.strptime(val, '%Y-%m-%d %H:%M:%S')
            month = val_datetime.month
            year = val_datetime.year
            if month == now_month and year == now_year:
                injury_counter += 1
    list_of_sum_data.append(injury_counter)


def get_column_to_insert(work_sheet):
    for number in range(1, 10000000000):
        val = work_sheet.cell(row=1, col=number).value
        if val == None:
            return number


def sheet_connection():
    scope = [
        "https://www.googleapis.com/auth/spreadsheets"
    ]
    creds = Credentials.from_service_account_file("shay-naama-9a0881eb1ec4.json", scopes=scope)
    client = gspread.authorize(creds)
    sheet_id = "12mIx8jTPaC5OzABlIL1j4OJf823GRr3Nb2WzY8jwvDk"
    sheet = client.open_by_key(sheet_id)
    return sheet


if __name__ == '__main__':
    sheet = sheet_connection()
    read_amount_of_injury_reports()
    insert_data_to_statistic()
    insert_data_to_class()










