from easypeasy_app import app, db

from flask_migrate import Migrate

migrate = Migrate(app, db)


class Meals(db.Model):
    __tablename__ = "meals"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Ingredients(db.Model):
    __tablename__ = "ingredients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


meal_ingredients = db.Table(
    "meal_ingredients",
    db.Column("meal_id", db.Integer, db.ForeignKey("meals.id"), primary_key=True),
    db.Column(
        "ingredient_id", db.Integer, db.ForeignKey("ingredients.id"), primary_key=True
    ),
)
