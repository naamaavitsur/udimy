from flask import Flask, render_template
import requests



app = Flask(__name__)

@app.route("/")
def find_age():
    response = requests.post(f"https://api.agify.io?name=naama")
    return render_template("index.html", response=response)


if __name__ == '__main__':
    app.run(debug=True)
