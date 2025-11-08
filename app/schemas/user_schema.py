from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    age = fields.Int(required=True, validate=validate.Range(min=1))
