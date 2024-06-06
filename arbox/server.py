import os
from flask import Flask, render_template, redirect, url_for
import google_sheet.insert_data as insert_data
from monthly_statistic.get_dates import get_default_start_end_dates

app = Flask(__name__, template_folder='flask_server/templates', static_folder='flask_server/static')


@app.route('/generate-statistic')
def generate_statistic():
    start_date, end_date = get_default_start_end_dates()
    insert_data.main(start_date,end_date)
    return render_template("done_page.html")


@app.route("/")
def home():
    return render_template("monthly_statistic.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
