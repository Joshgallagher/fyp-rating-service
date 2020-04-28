from tests.base_test import BaseTest
from rating.model.rating import Rating


class RatingTest(BaseTest):
    def test_create_rating(self):
        user_id = '854c9a9b-4a4a-410f-867c-9985c17878d8'
        article_id = 1

        Rating(user_id=user_id, article_id=article_id).save()

        self.assertIsNotNone(Rating.objects.get(
            user_id=user_id, article_id=article_id))
