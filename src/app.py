from flask import Flask, request, Response
from core.database import init_connection
from rating.model.rating import Rating

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://root:example@rating-service-db:27017/rating?authSource=admin'
}
init_connection(app)


@app.route('/<article>', methods=['GET'])
def get(article):
    rating = Rating.objects(articleId=article).count()
    return {'rating': int(rating)}, 200


@app.route('/', methods=['POST'])
def create():
    body = request.get_json()
    rating = Rating(**body).save()
    id = rating.id
    return {'id': str(id)}, 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
