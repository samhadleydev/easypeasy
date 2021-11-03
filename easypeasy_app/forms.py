from flask_wtf import FlaskForm as Form
from flask_wtf.recaptcha import validators
from wtforms import StringField
from wtforms.fields.core import SelectMultipleField
from wtforms.validators import DataRequired

from easypeasy_app.models import Ingredients

ingredient_choices = []


class MealForm(Form):
    name = StringField("name")
    ingredients = StringField("ingredients")
