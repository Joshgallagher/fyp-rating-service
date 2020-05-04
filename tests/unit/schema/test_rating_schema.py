from unittest import TestCase
from marshmallow import ValidationError
from src.rating.schema.rating_schema import RatingSchema


class RatingSchemaTest(TestCase):
    def test_rating_schema_validation_pass(self):
        article_id = 1

        try:
            RatingSchema().load({'articleId': article_id})
        except ValidationError:
            self.fail('Rating Schema validation failed.')

    def test_rating_schema_validation_fail(self):
        article_id_not_integer = 't'

        try:
            RatingSchema().load({'articleId': article_id_not_integer})
        except ValidationError as e:
            self.assertEqual(e.valid_data, {})
            self.assertEqual(
                e.messages, {'articleId': ['Not a valid integer.']})

        self.assertRaises(ValidationError)

        article_id_none = None

        try:
            RatingSchema().load({'articleId': article_id_none})
        except ValidationError as e:
            self.assertEqual(e.valid_data, {})
            self.assertEqual(
                e.messages, {'articleId': ['Field may not be null.']})

        self.assertRaises(ValidationError)
