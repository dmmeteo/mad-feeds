import os

from flask import Flask, jsonify
from flask_mongoengine import MongoEngine
from flask_debugtoolbar import DebugToolbarExtension

db = MongoEngine()


def create_app():
    # instantiate the app
    app = Flask(__name__)
    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    db.init_app(app)
    toolbar = DebugToolbarExtension(app)