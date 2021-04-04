from marshmallow import Schema

class UserSchema(Schema):

    class Meta:
        fields = ('pk_user', 'username', 'password')
        ordered = True

users_schema = UserSchema(many=True)
user_schema = UserSchema()
