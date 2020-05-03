from unittest import TestCase
from src.rating.model.rating import Rating


class RatingTest(TestCase):
    def test_create_rating(self):
        user_id = '854c9a9b-4a4a-410f-867c-9985c17878d8'
        article_id = 1

        rating = Rating(user_id=user_id, article_id=article_id)

        self.assertEqual(str(rating.user_id), user_id)
        self.assertEqual(rating.article_id, article_id)
