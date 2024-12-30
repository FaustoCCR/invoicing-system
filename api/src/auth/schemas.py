from marshmallow import Schema, fields


class LoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)


class TokenSchema(Schema):
    access_token = fields.String()
    token_type = fields.String(default="bearer")
