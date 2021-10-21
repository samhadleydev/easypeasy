from flask.json import jsonify
from easypeasy_app import app, request
from models import Meals


@app.route("/meals/create", methods=["POST"])
def create_meal():
    error = False
    body = {}
    name = request.get_json()["name"]
    meal = Meals(name=name)
    body["name"] = meal.name
    return jsonify(body)
