"""Package & module import."""
from flask import Flask

app = Flask(__name__)

from generator.main.routes import main

app.register_blueprint(main)
