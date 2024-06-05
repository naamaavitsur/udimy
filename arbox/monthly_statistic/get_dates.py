from datetime import datetime, timedelta
import calendar



def get_previous_month_date(date):
    if date.month == 1:
        previous_month_date = datetime(date.year - 1, 12, 1)
    else:
        previous_month_date = datetime(date.year, date.month - 1, 1)
    return previous_month_date.strftime("%m")


def find_last_month_year(current_year, previous_month):
    if previous_month == 1:
        last_month_year = current_year-1
        return last_month_year
    else:
        last_month_year = current_year
        return last_month_year


today = datetime.now()
current_day = today.day
current_month = today.month
current_year = today.year
previous_month = get_previous_month_date(today)
last_month_year = find_last_month_year(current_year, previous_month)
last_day_of_month = calendar.monthrange(current_year, current_month)[1]
seven_days_before_last_day = last_day_of_month - 7
formated_last_day_of_month= f"{last_month_year}-{previous_month}-{last_day_of_month}"
formated_last_seven_day_of_month =f"{last_month_year}-{previous_month}-{seven_days_before_last_day}"
formated_first_day_of_month = f"{last_month_year}-{previous_month}-01"
last_day_datetime_formate = datetime(year=last_month_year, month=int(previous_month), day=last_day_of_month)
seven_days_before_last_day_datetime_formate = last_day_datetime_formate + timedelta(-7)
last_day_dats_with_letters = last_day_datetime_formate.strftime("%a %b %d %Y")
last_seven_day_dats_with_letters = seven_days_before_last_day_datetime_formate.strftime("%a %b %d %Y")

# print(f"to:{last_day_dats_with_letters} 00:00:00 GMT+0300\n"
#       f"from:{last_seven_day_dats_with_letters} 00:00:00 GMT+0300")
#
# 'to': 'Sun Jun 09 2024 00:00:00 GMT+0300',
# 'from': 'Sun Jun 02 2024 00:00:00 GMT+0300',
# ("to: Thu May 30 2024 00:00:00 GMT+0300"
#  "from:Thu May 23 2024 00:00:00 GMT+0300")