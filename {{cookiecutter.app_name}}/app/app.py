# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
from app.settings import ProdConfig
from app.extensions import (
    db,
    migrate,
    api_scaffold,
)


basic_auth = HTTPBasicAuth()

def create_app(config_object=ProdConfig):
    """An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    CORS(app)

    @basic_auth.get_password
    def get_pw(username):
        return app.config['HTTP_BASICAUTH_PASSWORD']

    register_extensions(app)
    register_blueprints(app)
    register_extra(app)
    return app


def register_extensions(app):
    decorators = []
    decorators += [basic_auth.login_required]

    db.init_app(app)
    migrate.init_app(app, db)
    api_scaffold.init_app(app, db, decorators)
    return None


def register_blueprints(app):
    return None


def register_extra(app):

    from flask import send_from_directory

    @app.route('/', methods=['GET'])
    def index():
        return send_from_directory('static', 'index.html')
