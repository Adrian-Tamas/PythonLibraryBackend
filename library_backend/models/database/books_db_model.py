import json

from sqlalchemy import Column, String, Boolean

from library_backend import Base
from library_backend.models.database.sqlalchemy_serializer import SQLAlchemySerializer


class BooksDBModel(Base, SQLAlchemySerializer):
    __tablename__ = f'books'

    book_id = Column(String, primary_key=True)
    book_name = Column(String)
    book_author = Column(String)
    book_is_reserved = Column(Boolean)

    def __init__(self, **fields):
        self.book_id = fields.get("book_id", None)
        self.book_name = fields["book_name"]
        self.book_author = fields["book_author"]
        self.book_is_reserved = fields.get("book_is_reserved", False)

    def __repr__(self):
        return f"{json.dumps(self.serialize())}"
