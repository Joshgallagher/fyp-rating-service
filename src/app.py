from flask import Flask
from core.database import init_connection
from flask_restful import Api
from core.routes import init_routes

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://root:example@rating-service-db:27017/rating?authSource=admin'
}

init_connection(app)
init_routes(api)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
