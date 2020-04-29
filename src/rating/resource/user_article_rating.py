from flask import g
from flask_restful import Resource
from rating.model.rating import Rating
from middleware.get_subject import get_subject
from middleware.authorise import authorise


class UserArticleRatingResource(Resource):
    method_decorators = [authorise, get_subject]

    def get(self, id):
        user_id = g.current_user_id
        rating = Rating.objects(user_id=user_id, article_id=id).count()
        return {'rating': int(rating)}, 200
