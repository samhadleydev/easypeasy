from os import name
from flask.json import jsonify
from flask.templating import render_template
from easypeasy_app import app, request, flash
from easypeasy_app.forms import MealForm
from models import Ingredients, Meals, db


@app.route("/")
def index():
    return render_template("pages/hello.html")


@app.route("/meals/create", methods=["GET"])
def create_meal_form():

    form = MealForm()

    return render_template("pages/hello.html", form=form)


@app.route("/meals/create", methods=["POST"])
def create_meal_submission():

    form = MealForm()

    name = form.name.data
    ingredients = form.ingredients.data

    new_meal = Meals(name=name, ingredients=ingredients)

    for ingredient in ingredients:
        get_ingredient = Ingredients.query.filter_by(name=ingredient).one_or_none()
        if get_ingredient:
            new_meal.ingredients.append(get_ingredient)
        else:
            new_ingredient = Ingredients(name=ingredient)
            db.session.add(new_ingredient)
            new_meal.ingredients.append(new_ingredient)

    try:
        db.session.add(new_meal)
        db.session.commit()
        flash("Yay!")
    except:
        flash("Noooo!")
    finally:
        db.session.close()
    return render_template("pages/hello.html")
