"""Package & module import."""
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

db = PyMongo(app)

from generator.main.routes import main

app.register_blueprint(main)
