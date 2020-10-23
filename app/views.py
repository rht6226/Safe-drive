from app import app, model
from flask import render_template
from flask import render_template
from flask import request
from flask import jsonify
from .drive import model_response

@app.route("/", methods=["GET"])
def greet():
    return "Drive Safe API is up and running"

@app.route("/drive", methods=["POST"])
def show():
    message = request.get_json(force=True)
    encoded_image = message['image']
    response = model_response(model, encoded_image)
    return jsonify(response)

    