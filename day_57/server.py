from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    random_number = random.randint(0,10)
    today_year = datetime.now().year
    return render_template("index.html", num=random_number, year=today_year)


if __name__ == '__main__':
    app.run(debug=True)
