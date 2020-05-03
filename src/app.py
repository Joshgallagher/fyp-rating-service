from flask import Flask
from flask_restful import Api
from src.core.database import init_connection
from src.core.routes import init_routes
from src.core.config import configure_app


def create_app(config_object=None):
    app = Flask(__name__)
    api = Api(app)

    if config_object is not None:
        app.config.from_object(config_object)
    else:
        configure_app(app)

    init_connection(app)
    init_routes(api)

    return app
