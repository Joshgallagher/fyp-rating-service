from flask import g, request
from flask_restful import Resource
from rating.model.rating import Rating
from middleware.get_subject import get_subject
from middleware.authorise import authorise
from rating.schema.rating_schema import RatingSchema
from marshmallow import ValidationError


class RatingResource(Resource):
    method_decorators = {'post': [authorise, get_subject]}

    def get(self, id):
        rating = Rating.objects(article_id=id).count()

        return {'rating': int(rating)}, 200

    def post(self):
        user_id = g.current_user_id

        try:
            article_id = request.get_json()['articleId']
        except Exception:
            article_id = None

        try:
            RatingSchema().load({'articleId': article_id})
        except ValidationError as e:
            return e.messages, 422

        count = Rating.objects(user_id=user_id, article_id=article_id).count()
        if count == 50:
            return {
                'message':
                    'You have given this article the maximum rating possible'
            }, 403

        Rating(user_id=user_id, article_id=article_id).save()

        return {'rated': True}, 201
