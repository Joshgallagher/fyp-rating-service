import json

from tests.integration.integration_base_test import IntegrationBaseTest
from unittest.mock import patch
from rating.model.rating import Rating


class RatingTest(IntegrationBaseTest):
    def setUp(self):
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': 'Bearer {}'.format(self.token)}

        super().setUp()

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

            payload = json.dumps({'articleId': 1})
            request = self.app.post(
                '/ratings', headers=self.headers, data=payload)

            self.assertEqual(json.dumps(
                {'rated': True}), json.dumps(request.json))
            self.assertEqual(201, request.status_code)

    def test_create_rating_validation(self):
        with patch('middleware.get_jwk.get_jwk') as get_jwk:
            get_jwk.return_value = json.dumps(self.jwk)

            payload = json.dumps({'articleId': 't'})
            request = self.app.post(
                '/ratings', headers=self.headers, data=payload)

            self.assertEqual(json.dumps(
                {'articleId': ['Not a valid integer.']}),
                json.dumps(request.json))
            self.assertEqual(422, request.status_code)

            payload = json.dumps({'articleId': None})
            request = self.app.post(
                '/ratings', headers=self.headers, data=payload)

            self.assertEqual(json.dumps(
                {'articleId': ['Field may not be null.']}),
                json.dumps(request.json))
            self.assertEqual(422, request.status_code)
