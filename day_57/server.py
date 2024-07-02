from flask import Flask, render_template
import requests



app = Flask(__name__)


@app.route(f"/guess/<name>")
def find_age(name):
    response = requests.get(f"https://api.agify.io/?name={name}")
    age = response.json()["age"]
    return render_template("index.html", name=name, age=age)

@app.route("/blog")
def write_blog():
    response = requests.get("https://api.npoint.io/33acc64b78645f6c2fd3")
    all_posts = response.json()
    return render_template("blog.html", blog_posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
