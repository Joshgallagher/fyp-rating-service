from flask import request
from flask_restful import Resource
from src.rating.model.rating import Rating


class RatingsResource(Resource):
    def post(self):
        try:
            ids = request.get_json()['articleIds']
        except Exception:
            ids = None

        if ids is None or not ids:
            return {'message': 'No articleIds have been provided.'}, 422

        pipeline = [
            {
                '$group': {
                    '_id': '$article_id',
                    'rating': {'$sum': 1}
                }
            },
            {
                '$project': {
                    '_id': 0,
                    'articleId': '$_id',
                    'rating': 1,
                }
            },
            {
                '$sort': {
                    'articleId': 1
                }
            }
        ]
        rating = Rating.objects(article_id__in=ids).aggregate(pipeline)

        return list(rating), 200
