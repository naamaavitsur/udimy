import os
from flask import Flask, render_template, redirect, url_for, request
import google_sheet.insert_data as insert_data
from monthly_statistic.get_dates import get_default_start_end_dates
from datetime import datetime


app = Flask(__name__, template_folder='flask_server/templates', static_folder='flask_server/static')


@app.route('/generate-statistic', methods=["POST"])
def generate_statistic():
    start_date = request.form.get("from")
    end_date = request.form.get("to")
    start_date = datetime(year=int(start_date[:4]),month=int(start_date[5:7]), day=int(start_date[8:]))
    end_date = datetime(year=int(end_date[:4]),month=int(end_date[5:7]), day=int(end_date[8:]))
    insert_data.main(start_date, end_date)
    return render_template("done_page.html")


@app.route("/")
def home():
    start_date, end_date = get_default_start_end_dates()
    from_date = start_date.strftime('%Y-%m-%d')
    to_date = end_date.strftime('%Y-%m-%d')
    return render_template("monthly_statistic.html", from_date=from_date, to_date=to_date)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
