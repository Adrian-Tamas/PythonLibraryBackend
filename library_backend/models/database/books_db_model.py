from sqlalchemy import Column, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BooksDBModel(Base):
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

