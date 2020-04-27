from flask import g
from flask_restful import Resource
from rating.model.rating import Rating
from middleware.get_subject import get_subject
# from middleware.authorise import authorise


class RatingsResource(Resource):
    # method_decorators = {'post': [authorise, get_subject]}
    method_decorators = {'post': [get_subject]}

    def get(self, id):
        rating = Rating.objects(articleId=id).count()
        return {'rating': int(rating)}, 200

    def post(self, id):
        userId = g.current_user_id
        rating = Rating(userId=userId, articleId=id).save()
        id = rating.id
        return {'id': str(id)}, 201
