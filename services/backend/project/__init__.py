import os

from flask import Flask, jsonify
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_debugtoolbar import DebugToolbarExtension
from .response import make_rss_response


api = Api(prefix='/api', default_mediatype='application/xml')
api.representations['application/xml'] = make_rss_response
db = MongoEngine()


def create_app():
    # instantiate the app
    app = Flask(__name__)
    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    db.init_app(app)
    # toolbar = DebugToolbarExtension(app)

    # Hook up resources and the API extension.
    from .app.v1.resources import FacebookProductFeed
    api.add_resource(FacebookProductFeed, '/v1/facebook_rss/<string:entry>')

    api.init_app(app)
    return app



