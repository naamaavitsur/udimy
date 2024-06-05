from arbox.monthly_statistic.get_arbox_data import get_token, get_active_user, count_member_type, get_cancelation, cancellation_fee, get_schedule_data
from datetime import datetime
from monthly_statistic.get_dates import last_day_datetime_formate



token = get_token()
date = last_day_datetime_formate.strftime("%Y-%m")
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
monthly_cancelation = get_cancelation(token=token)
number_of_cancellation_fee = cancellation_fee(token)
list_of_class_data = get_schedule_data(token)
list_of_sum_data = [date, all_monythly_only, all_renewable, all_renewable+all_monythly_only,monthly_cancelation,number_of_cancellation_fee]

