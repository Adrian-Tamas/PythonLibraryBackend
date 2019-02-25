from sqlalchemy import Column, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UsersDBModel(Base):
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

