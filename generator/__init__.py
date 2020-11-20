"""Package & module import."""
import os
from flask import Flask
from flask_pymongo import PyMongo
from generator.config import Config

app = Flask(__name__)
app.config.from_object(Config)

mongo = PyMongo(app)
db = mongo.db

from generator.main.routes import main

app.register_blueprint(main)
