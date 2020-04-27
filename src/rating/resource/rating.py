from flask import request
from rating.model.rating import Rating
from flask_restful import Resource


class RatingsResource(Resource):
    def get(self, id):
        rating = Rating.objects(articleId=id).count()
        return {'rating': int(rating)}, 200

    def post(self, id):
        userId = request.get_json()['userId']
        rating = Rating(userId=userId, articleId=id).save()
        id = rating.id
        return {'id': str(id)}, 201
