from flask import Flask, render_template
app = Flask(__name__)

@app.route("/second")
def second():
    print("im so cool")
    return render_template("second_edit.html")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)