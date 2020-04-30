from marshmallow import Schema, fields, validate


class RatingSchema(Schema):
    article_id = fields.Integer(
        required=True, validate=validate.Range(min=1), data_key='articleId')
