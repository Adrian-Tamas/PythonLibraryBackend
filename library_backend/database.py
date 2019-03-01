import uuid
from datetime import datetime
from functools import wraps

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from library_backend import logger, Base
from library_backend.models.database.books_db_model import BooksDBModel
from library_backend.models.database.reservations_db_model import ReservationsDBModel
from library_backend.models.database.users_db_model import UsersDBModel


def check_session():
    """
    Decorator function to check if the session has been initialized

    :return: callable
    :raises Exception
    """

    def check_session_wrapper(callable_func):
        @wraps(callable_func)
        def decor_inner(instance, *args, **kwargs):
            if not instance.session:
                raise AttributeError('No session. Please use context manager.')
            return callable_func(instance, *args, **kwargs)
        return decor_inner
    return check_session_wrapper


class SQLiteDatabaseConnection:

    def __init__(self):
        self.engine = create_engine("sqlite:///db.sqlite", echo=False)
        self.session = None
        self.connection_name = None

    def __enter__(self):
        self.session = sessionmaker(bind=self.engine)()

    @check_session()
    def create_tables_if_not_exists(self):
        try:
            if not (self.engine.dialect.has_table(self.engine, UsersDBModel.__tablename__)
                    and self.engine.dialect.has_table(self.engine, BooksDBModel.__tablename__)
                    and self.engine.dialect.has_table(self.engine, ReservationsDBModel.__tablename__)):
                logger.info(f"Creating table {UsersDBModel.__tablename__}...")
                try:
                    Base.metadata.create_all(self.engine)
                except Exception as ex:
                    logger.error(ex)
                logger.info(f"Created table {UsersDBModel.__tablename__}...")
            else:
                logger.info(f"Table {UsersDBModel.__tablename__} already exists!")
        except SQLAlchemyError as e:
            logger.error(e, exc_info=True)
            raise

    @check_session()
    def add_user(self, user_model: UsersDBModel):
        user_id = str(uuid.uuid4())
        user_model.user_id = user_id
        self.session.add(user_model)

    @check_session()
    def add_book(self, book_model: BooksDBModel):
        book_id = str(uuid.uuid4())
        book_model.book_id = book_id
        self.session.add(book_model)

    @check_session()
    def add_reservation(self, reservation_model: ReservationsDBModel):
        self.session.add(reservation_model)

    @check_session()
    def get_all_users(self):
        return self.session.query(UsersDBModel).all()

    @check_session()
    def get_users_by_first_and_last_name(self, first_name, last_name):
        return self.session.query(UsersDBModel)\
            .filter(UsersDBModel.user_first_name == first_name,
                    UsersDBModel.user_last_name == last_name).all()

    @check_session()
    def get_user_by_email(self, email):
        return self.session.query(UsersDBModel).filter(UsersDBModel.user_email == email).one_or_none()

    @check_session()
    def get_all_books(self):
        return self.session.query(BooksDBModel).all()

    @check_session()
    def get_books_by_name(self, name):
        return self.session.query(BooksDBModel).filter(BooksDBModel.book_name == name).all()

    @check_session()
    def get_books_by_author(self, author):
        return self.session.query(BooksDBModel).filter(BooksDBModel.book_author == author).all()

    @check_session()
    def get_book_by_author_and_name(self, author, name):
        return self.session.query(BooksDBModel)\
            .filter(BooksDBModel.book_author == author,
                    BooksDBModel.book_name == name).one_or_none()

    @check_session()
    def get_books_by_partial_author_name(self, partial_name):
        return self.session.query(BooksDBModel) \
                   .filter(BooksDBModel.book_author.ilike(f'%{partial_name}%')).all()

    @check_session()
    def get_reserved_books(self):
        user, books = self.session.query(UsersDBModel, BooksDBModel)\
            .join(UsersDBModel.user_id == ReservationsDBModel.user_id and BooksDBModel.book_id == BooksDBModel.book_id).all()
        print("test")
        return  #TODO: check multijoin

    @check_session()
    def add_some_data_if_does_not_exist(self):
        user1 = UsersDBModel(user_email="adi.tamas@endava.com", user_first_name="Adrian", user_last_name="Tamas")
        user2 = UsersDBModel(user_email="ion.ionescu@endava.com", user_first_name="Ion", user_last_name="Ionescu")
        book1 = BooksDBModel(book_name="A song of ice and fire", book_author="George R.R. Martin")

        nr_of_entries = self.session.query(UsersDBModel).count()
        if nr_of_entries is 0:
            self.add_user(user1)
            self.add_user(user2)

        nr_of_entries = self.session.query(BooksDBModel).count()
        if nr_of_entries is 0:
            self.add_book(book1)

        nr_of_entries = self.session.query(ReservationsDBModel).count()
        if nr_of_entries is 0:
            reservation = ReservationsDBModel(book_id=book1.book_id, user_id=user1.user_id, reservation_expiration_date= None, reservation_date=f"{datetime.now()}")
            self.add_reservation(reservation)

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.session.rollback()
            self.session.close()
            return False
        else:
            try:
                self.session.commit()
            except Exception as err:
                logger.error(f"Commit failed: {err}")
                self.session.rollback()
                self.session.close()
        self.session.close()
