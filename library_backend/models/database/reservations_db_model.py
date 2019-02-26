from sqlalchemy import Column, String, ForeignKey

from library_backend import Base
from library_backend.models.database.books_db_model import BooksDBModel
from library_backend.models.database.users_db_model import UsersDBModel


class ReservationsDBModel(Base):
    __tablename__ = f'reservations'

    book_id = Column(String, ForeignKey(BooksDBModel.book_id), primary_key=True)
    user_id = Column(String, ForeignKey(UsersDBModel.user_id), primary_key=True)
    reservation_date = Column(String)
    reservation_expiration_date = Column(String)

    def __init__(self, **fields):
        self.book_id = fields.get("book_id")
        self.user_id = fields["user_id"]
        self.reservation_date = fields["reservation_date"]
        self.reservation_expiration_date = fields.get("reservation_expiration_date")
