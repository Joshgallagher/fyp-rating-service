from flask import g
from flask_restful import Resource
from rating.model.rating import Rating
from middleware.get_subject import get_subject
# from middleware.authorise import authorise


class RatingsResource(Resource):
    # method_decorators = {'post': [authorise, get_subject]}
    method_decorators = {'post': [get_subject]}

    def get(self, id):
        rating = Rating.objects(article_id=id).count()
        return {'rating': int(rating)}, 200

    def post(self, id):
        user_id = g.current_user_id
        count = Rating.objects(user_id=user_id, article_id=id).count()
        if count == 50:
            return {
                'message':
                    'You have given this article the maximum rating possible'
            }, 403
        Rating(user_id=user_id, article_id=id).save()
        return {'rated': True}, 201


class UserArticleRatingResource(Resource):
    # method_decorators = [authorise, get_subject]
    method_decorators = [get_subject]

    def get(self, id):
        user_id = g.current_user_id
        rating = Rating.objects(user_id=user_id, article_id=id).count()
        return {'rating': int(rating)}, 200
