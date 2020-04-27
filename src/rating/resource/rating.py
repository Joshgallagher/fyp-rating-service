from flask import request
from flask_restful import Resource
from rating.model.rating import Rating
from middleware.user_id_header import user_id_header


class RatingsResource(Resource):
    method_decorators = {'post': [user_id_header]}

    def get(self, id):
        rating = Rating.objects(articleId=id).count()
        return {'rating': int(rating)}, 200

    def post(self, id):
        userId = request.get_json()['userId']
        rating = Rating(userId=userId, articleId=id).save()
        id = rating.id
        return {'id': str(id)}, 201
