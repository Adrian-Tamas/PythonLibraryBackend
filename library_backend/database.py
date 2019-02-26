import os
import uuid
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
        self.engine = create_engine("sqlite:///db.sqlite", echo=True)
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

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.session.rollback()
            self.session.close()
            return False
        else:
            try:
                self.session.commit()
            except Exception as err:
                self.session.rollback()
                self.session.close()
                logger.error(err)
        self.session.close()
