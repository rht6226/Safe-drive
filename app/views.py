from app import app, model
from flask import render_template
from flask import render_template
from flask import request
from flask import jsonify
from .drive import model_response



# @app.route('/', methods=['GET'])
# def test():
#     return render_template('index.html')


# @app.route("/predict", methods=["POST"])
# def predict():
#     message = request.get_json(force=True)
#     encoded_image = message['image']
#     response = model_response(model, encoded_image)
#     return jsonify(response)


# @app.route("/image", methods=["POST"])
# def show():
#     message = request.get_json(force=True)
#     encoded_image = message['image']
#     show_image(encoded_image)
#     response = {
#         'data': 'OKAY'
#     }
#     return jsonify(response)

@app.route("/drive", methods=["POST"])
def show():
    message = request.get_json(force=True)
    encoded_image = message['image']
    response = model_response(model, encoded_image)
    return jsonify(response)

    