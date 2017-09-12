# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
from flask import Flask

from app.settings import ProdConfig
from app.extensions import (
    db,
    migrate,
    api_scaffold,
)


def create_app(config_object=ProdConfig):
    """An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_extra(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    api_scaffold.init_app(app, db)
    return None


def register_blueprints(app):
    return None


def register_extra(app):

    from flask import send_from_directory

    @app.route('/', methods=['GET'])
    def index():
        return send_from_directory('static', 'index.html')
