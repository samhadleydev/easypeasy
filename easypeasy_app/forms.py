from flask_wtf import FlaskForm as Form
from flask_wtf.recaptcha import validators
from wtforms import StringField
from wtforms.validators import DataRequired


class MealForm(Form):
    name = StringField("name", validators=[])
