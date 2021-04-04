from flask_jwt_extended import (
    create_access_token
)
from src.app.models.administration import User

class AuthService:
    _instance = None

    def get_token(self, **kwargs):
        try:
            verify_user = User.query.filter(
                User.username == kwargs['username'],
                User.password == kwargs['password']
            ).first()
            if verify_user:
                access_token = create_access_token(identity = kwargs['username'])
                return access_token
            return None
        except:
            return None