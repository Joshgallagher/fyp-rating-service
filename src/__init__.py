from flask import Flask
from src.core.database import init_connection
from flask_restful import Api
from src.core.routes import init_routes

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://root:example@rating-service-db:27017/rating-test?authSource=admin'
}

init_connection(app)
init_routes(api)
