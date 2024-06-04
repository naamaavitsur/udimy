import os
from googleapiclient.discovery import build

# client_id = os.getenv("CLIENTID")
# print(client_id)
# client_secret = os.getenv("CLIENTSECRET")
API_KEY = os.getenv("API_KEY")


def authenticate_sheets(api_key):
    return build('sheets', 'v4', developerKey=api_key).spreadsheets()


def read_data(api_key, spreadsheet_id, sheet_name, start_cell, end_cell):
    range_name= f"{sheet_name}!{start_cell}:{end_cell}"
    sheets = authenticate_sheets(api_key)
    result = sheets.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])
    print(values)


if __name__ == '__main__':
    SPREADSHEET_ID = '12mIx8jTPaC5OzABlIL1j4OJf823GRr3Nb2WzY8jwvDk'
    RANGE_NAME = 'naama!A1:E26'
    read_data(API_KEY, SPREADSHEET_ID, "naama", "A1", "E26")

