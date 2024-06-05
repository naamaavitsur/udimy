from datetime import datetime, timedelta
import calendar
import config


def get_previous_month_date(date) -> int:
    if date.month == 1:
        previous_month_date = 12
    else:
        previous_month_date = date.month - 1
    return previous_month_date


def find_last_month_year(current_year, previous_month):
    if previous_month == 12:
        last_month_year = current_year-1
        return last_month_year
    return current_year


def get_default_end_dates():
    now = datetime.now()
    current_year = now.year
    previous_month = get_previous_month_date(now)
    last_month_year = find_last_month_year(current_year, previous_month)
    last_day_of_month = calendar.monthrange(last_month_year, previous_month)[1]  # number of days in the month
    return (datetime(last_month_year, previous_month, 1),
            datetime(last_month_year, previous_month, last_day_of_month))


def get_start_and_end_for_last_week_of_last_month():
    last_day_of_month = get_default_end_dates()[1]
    week_before_end_day = last_day_of_month - timedelta(days=7)
    return week_before_end_day, last_day_of_month



formated_last_day_of_month= f"{last_month_year}-{previous_month}-{last_day_of_month}"
formated_last_seven_day_of_month =f"{last_month_year}-{previous_month}-{seven_days_before_last_day}"
formated_first_day_of_month = f"{last_month_year}-{previous_month}-01"
last_day_dats_with_letters = last_day_datetime_formate.strftime("%a %b %d %Y")
last_seven_day_dats_with_letters = seven_days_before_last_day_datetime_formate.strftime("%a %b %d %Y")



# print(f"to:{last_day_dats_with_letters} 00:00:00 GMT+0300\n"
#       f"from:{last_seven_day_dats_with_letters} 00:00:00 GMT+0300")
#
# 'to': 'Sun Jun 09 2024 00:00:00 GMT+0300',
# 'from': 'Sun Jun 02 2024 00:00:00 GMT+0300',
# ("to: Thu May 30 2024 00:00:00 GMT+0300"
#  "from:Thu May 23 2024 00:00:00 GMT+0300")


if __name__ == '__main__':
    print(get_default_end_dates())
    print(get_start_and_end_for_last_week_of_last_month())