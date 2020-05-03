import json

from tests.integration.integration_base_test import IntegrationBaseTest
from unittest.mock import patch
from src.rating.model.rating import Rating


class RatingTest(IntegrationBaseTest):
    def setUp(self):
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': 'Bearer {}'.format(self.token)}

        super().setUp()

    def test_get_article_ratings_by_ids(self):
        with patch('src.middleware.get_jwk.get_jwk') as get_jwk:
            get_jwk.return_value = json.dumps(self.jwk)

            user_id = self.token_subject
            other_user_id = '83998496-2638-436e-9dc0-c04b5de5a2ce'

            Rating(user_id=user_id, article_id=1).save()
            Rating(user_id=other_user_id, article_id=1).save()
            Rating(user_id=user_id, article_id=2).save()
            Rating(user_id=other_user_id, article_id=3).save()
            Rating(user_id=other_user_id, article_id=4).save()

            payload = json.dumps({'articleIds': [1, 2]})
            request = self.app.post(
                '/ratings/users', headers=self.headers, data=payload)

            self.assertDictEqual(
                {'rating': 2, 'articleId': 1}, request.json[0])
            self.assertDictEqual(
                {'rating': 1, 'articleId': 2}, request.json[1])
            self.assertEqual(200, request.status_code)

    def test_get_article_ratings_by_ids_validation(self):
        with patch('src.middleware.get_jwk.get_jwk') as get_jwk:
            get_jwk.return_value = json.dumps(self.jwk)

            payload = json.dumps({'articleIds': []})
            request = self.app.post(
                '/ratings/users', headers=self.headers, data=payload)

            self.assertEqual(json.dumps(
                {"message": "No articleIds have been provided."}),
                json.dumps(request.json))
            self.assertEqual(422, request.status_code)
