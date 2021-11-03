from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object("easypeasy_app.config")
db = SQLAlchemy(app)
