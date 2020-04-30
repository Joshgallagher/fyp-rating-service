import json

from tests.integration.integration_base_test import IntegrationBaseTest
from unittest.mock import patch
from rating.model.rating import Rating


class UserArticleRatingTest(IntegrationBaseTest):
    def test_get_user_article_rating(self):
        with patch('middleware.get_jwk.get_jwk') as get_jwk:
            get_jwk.return_value = json.dumps(self.jwk)

            token = 'Bearer {}'.format(self.token)
            article_id = 1

            user_id = self.token_subject
            other_user_id = '83998496-2638-436e-9dc0-c04b5de5a2ce'

            Rating(user_id=user_id, article_id=article_id).save()
            Rating(user_id=other_user_id, article_id=article_id).save()

            request = self.app.get(
                '/ratings/{}/user'.format(article_id),
                headers={'Authorization': token})

            self.assertEqual(json.dumps(
                {'rating': 1}), json.dumps(request.json))
            self.assertEqual(200, request.status_code)
