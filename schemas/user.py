from .base import ma 
from flask_marshmallow import Schema


class UserSchema(Schema):
    class Meta:
        fields = ['username', 'email']


user_schema = UserSchema()