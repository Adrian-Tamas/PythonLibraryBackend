import json
from sqlalchemy import Column, String

from library_backend import Base
from library_backend.models.database.sqlalchemy_serializer import SQLAlchemySerializer


class UsersDBModel(Base, SQLAlchemySerializer):
    __tablename__ = f'users'

    user_id = Column(String, primary_key=True)
    user_first_name = Column(String)
    user_last_name = Column(String)
    user_email = Column(String, unique=True)

    def __init__(self, **fields):
        self.user_id = fields.get("user_id", None)
        self.user_first_name = fields["user_first_name"]
        self.user_last_name = fields["user_last_name"]
        self.user_email = fields["user_email"]

    def __repr__(self):
        return f"{json.dumps(self.serialize())}"