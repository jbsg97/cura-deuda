from src.config.db import db
from src.app.serializers.administration import user_schema, users_schema
from src.app.models.administration import User
from sqlalchemy import exc as SQLAlchemyError

class UserService:
    _instance = None

    def create(self, **kwargs):
        data = User(**kwargs)
        try:
            db.session.add(data)
            db.session.commit()
            return user_schema.dump(data)
        except SQLAlchemyError as e:
            db.session.rollback()
            return None

    def fetch(self):
        users = User.query.all()
        return None if not users else users_schema.dump(users)
