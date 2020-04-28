from rating.resource.rating import RatingsResource, UserArticleRatingResource


def init_routes(api):
    api.add_resource(RatingsResource, '/ratings/<int:id>')
    api.add_resource(UserArticleRatingResource, '/ratings/user/<int:id>')
