import sys

from flask import g, request
from flask_restful import Resource
from rating.model.rating import Rating
from middleware.get_subject import get_subject


class RatingsResource(Resource):
    method_decorators = {'post': [get_subject]}

    def get(self, id):
        rating = Rating.objects(articleId=id).count()
        return {'rating': int(rating)}, 200

    def post(self, id):
        print('POST:' + g.current_user_id, file=sys.stderr)
        userId = request.get_json()['userId']
        rating = Rating(userId=userId, articleId=id).save()
        id = rating.id
        return {'id': str(id)}, 201
