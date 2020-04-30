from rating.resource.rating import RatingResource
from rating.resource.user_article_rating import UserArticleRatingResource


def init_routes(api):
    api.add_resource(RatingResource, '/ratings/<int:id>', '/ratings')
    api.add_resource(UserArticleRatingResource, '/ratings/<int:id>/user')
