from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    VARCHAR
)
from src.config.db import db

class User(db.Model):
    __tablename__ = 'usuarios'
    __table_args__ = {'implicit_returning': False}
    pk_user = Column(Integer, primary_key=True, nullable=False)
    username = Column(VARCHAR(length=250))
    password = Column(VARCHAR(length=250))
