import os

from flask import Flask, render_template, redirect, url_for
import sys
sys.path.append("../")
import google_sheet.insert_data as insert_data

app = Flask(__name__)


@app.route('/generate-statistic')
def generate_statistic():
    # Call your function here
    insert_data.main()
    print("Generating monthly statistic...")
    return redirect(url_for('/'))


@app.route("/")
def home():
    return render_template("monthly_statistic.html")

if __name__ == '__main__':
    app.run(debug=True)