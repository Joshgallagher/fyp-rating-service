from rating.resource.rating import RatingResource
from rating.resource.user_article_rating import UserArticleRatingResource
from rating.resource.ratings import RatingsResource


def init_routes(api):
    api.add_resource(RatingResource, '/ratings/<int:id>', '/ratings')
    api.add_resource(UserArticleRatingResource, '/ratings/<int:id>/user')
    api.add_resource(RatingsResource, '/ratings/users')
