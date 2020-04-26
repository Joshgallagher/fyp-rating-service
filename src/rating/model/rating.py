from core.database import database


class Rating(database.Document):
    userId = database.UUIDField(binary=False, required=True)
    articleId = database.IntField(required=True)
