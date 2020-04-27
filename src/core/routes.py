from rating.resource.rating import RatingsResource


def init_routes(api):
    api.add_resource(RatingsResource, '/ratings/<id>')
