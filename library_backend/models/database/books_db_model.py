import json

from sqlalchemy import Column, String

from library_backend import Base
from library_backend.models.database.sqlalchemy_serializer import SQLAlchemySerializer


class BooksDBModel(Base, SQLAlchemySerializer):
    __tablename__ = f'books'

    id = Column(String, primary_key=True)
    name = Column(String)
    author = Column(String)

    def __init__(self, **fields):
        self.id = fields.get("id", None)
        self.name = fields["name"]
        self.author = fields["author"]

    def __repr__(self):
        return f"{json.dumps(self.serialize())}"
