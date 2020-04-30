from flask import g
from flask_restful import Resource, reqparse
from rating.model.rating import Rating
from middleware.get_subject import get_subject
from middleware.authorise import authorise


class RatingResource(Resource):
    method_decorators = {'post': [authorise, get_subject]}

    def get(self, id):
        rating = Rating.objects(article_id=id).count()

        return {'rating': int(rating)}, 200

    def post(self):
        user_id = g.current_user_id

        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True,
                            help='An article ID is required')
        args = parser.parse_args()

        id = args['id']

        count = Rating.objects(user_id=user_id, article_id=id).count()
        if count == 50:
            return {
                'message':
                    'You have given this article the maximum rating possible'
            }, 403

        Rating(user_id=user_id, article_id=id).save()

        return {'rated': True}, 201
