from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object("easypeasy_app.config")
db = SQLAlchemy(app)


@app.route("/")
def hello_world():
    return render_template("pages/home.html")
