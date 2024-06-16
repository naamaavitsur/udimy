from monthly_statistic.get_arbox_data import get_token, get_active_user, count_member_type, get_cancelation, cancellation_fee, get_last_week_data, get_last_week_response
from monthly_statistic.get_dates import make_date_formated, get_previous_month_date, get_default_start_end_dates
import config


def create_stats_data_to_insert(token, start_date, end_date):
    date = make_date_formated(start_date, config.sheet_format)
    active_member = get_active_user(token=token)
    renewable_monthly = count_member_type(active_member=active_member, member_type="מנוי חודשי מתחדש")
    renewable_monthly_old = count_member_type(active_member, member_type="מנוי חודשי מתחדש הוק- ישן")
    renewable_monthly_student = count_member_type(active_member, member_type="מנוי חודשי מתחדש- סטודנטים")
    renewable_monthly_solders = count_member_type(active_member, member_type="מנוי חודשי מתחדש- חיילים")
    renewable_monthly_solders_old = count_member_type(active_member, 'מנוי חודשי מתחדש ישן- חיילים הו"ק')
    all_renewable = renewable_monthly + renewable_monthly_old + renewable_monthly_solders_old + renewable_monthly_student + renewable_monthly_solders
    monthly_only = count_member_type(active_member, "מנוי חודש בודד")
    monthly_only_sol_stu = count_member_type(active_member,"מנוי חודש בודד- חיילים/סטודנטים")
    all_monythly_only = monthly_only + monthly_only_sol_stu
    monthly_cancelation = get_cancelation(token, start_date, end_date)
    number_of_cancellation_fee = cancellation_fee(token, start_date, end_date)
    list_of_sum_data = [date, all_monythly_only, all_renewable, all_renewable+all_monythly_only, monthly_cancelation, number_of_cancellation_fee]
    return list_of_sum_data


def create_class_data(token):
    list_of_class_data = get_last_week_data(token)
    return list_of_class_data

if __name__ == '__main__':
    token = get_token()
    create_stats_data_to_insert(token)