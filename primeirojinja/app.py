from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def ambt():
    return render_template("ambt.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")
