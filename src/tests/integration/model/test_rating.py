from tests.integration.integration_base_test import IntegrationBaseTest
from rating.model.rating import Rating


class RatingTest(IntegrationBaseTest):
    def test_create_rating(self):
        user_id = self.token_subject
        article_id = 1

        Rating(user_id=user_id, article_id=article_id).save()

        self.assertIsNotNone(Rating.objects.get(
            user_id=user_id, article_id=article_id))
