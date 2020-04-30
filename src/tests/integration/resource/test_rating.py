import json

from tests.integration.integration_base_test import IntegrationBaseTest
from unittest.mock import patch
from rating.model.rating import Rating


class RatingTest(IntegrationBaseTest):
    def test_get_rating(self):
        article_id = 1
        user_id = self.token_subject

        Rating(user_id=user_id, article_id=article_id).save()

        request = self.app.get('/ratings/{}'.format(article_id))

        self.assertEqual(json.dumps({'rating': 1}), json.dumps(request.json))
        self.assertEqual(200, request.status_code)

    def test_create_rating(self):
        with patch('middleware.get_jwk.get_jwk') as get_jwk:
            get_jwk.return_value = json.dumps(self.jwk)

            token = 'Bearer {}'.format(self.token)
            headers = {'Content-Type': 'application/json',
                       'Authorization': token}

            payload = json.dumps({'id': 1})
            request = self.app.post('/ratings', headers=headers, data=payload)

            self.assertEqual(json.dumps(
                {'rated': True}), json.dumps(request.json))
            self.assertEqual(201, request.status_code)
