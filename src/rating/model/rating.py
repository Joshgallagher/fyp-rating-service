from datetime import datetime
from core.database import database


class Rating(database.Document):
    user_id = database.UUIDField(binary=False, required=True)
    article_id = database.IntField(required=True)
    created_at = database.DateTimeField(
        required=True, default=datetime.now())
