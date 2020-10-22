from flask import Flask
from flask_cors import CORS
from .drive import get_model


app = Flask(__name__)
CORS(app)

model = get_model()

from app import views