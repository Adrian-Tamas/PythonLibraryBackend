from library_backend.database import SQLiteDatabaseConnection
from library_backend.exceptions import UserAlreadyExists, InvalidUser, ResourceNotFound, InvalidFieldException, \
    BookAlreadyExists
from library_backend.models.database.books_db_model import BooksDBModel
from library_backend.models.database.users_db_model import *


class UserService:

    def create_user(self, user_dict):
        db = SQLiteDatabaseConnection()
        with db:
            if db.get_user_by_email(user_dict["email"]):
                raise UserAlreadyExists(user_dict)
        user_model = UsersDBModel(**user_dict)
        with db:
            db.add_user(user_model)
            user_dict = db.get_user_by_email(user_model.email).serialize()
        return user_dict

    def list_users(self):
        db = SQLiteDatabaseConnection()
        with db:
            user_list = UsersDBModel.serialize_list(db.get_all_users())
        return user_list

    def get_user(self, user_id):
        db = SQLiteDatabaseConnection()
        with db:
            user = db.get_user_by_id(user_id)
            if not user:
                raise ResourceNotFound(resource_type="User", field="user_id", value=user_id)
            user = user.serialize()

        return user

    def delete_user(self, user_id):
        db = SQLiteDatabaseConnection()
        with db:
            rows = db.delete_user_by_id(user_id)
        if rows == 0:
            raise ResourceNotFound(resource_type="User", field="user_id", value=user_id)

    def update_user(self, user_id, new_user):
        if new_user.get("id"):
            del new_user["id"]
        old_user = self.get_user(user_id)
        if not old_user["email"] == new_user["email"]:
            raise InvalidFieldException("email")
        db = SQLiteDatabaseConnection()
        user_model = UsersDBModel(id=user_id, **new_user)
        with db:
            rows = db.update_user(user_id, user_model)
        user = self.get_user(user_id)
        if rows == 0:
            raise Exception
        return user


class BookService:

    def create_book(self, book):
        db = SQLiteDatabaseConnection()
        with db:
            existing_book = db.get_book_by_author_and_name(author=book["author"], name=book["name"])
            if existing_book:
                raise BookAlreadyExists(book)
        book_model = BooksDBModel(**book)
        with db:
            db.add_book(book_model)
            book = db.get_book_by_author_and_name(name=book_model.name, author=book_model.author).serialize()
        return book

    def list_books(self):
        db = SQLiteDatabaseConnection()
        with db:
            books_list = BooksDBModel.serialize_list(db.get_all_books())
        return books_list

    def get_book(self, book_id):
        db = SQLiteDatabaseConnection()
        with db:
            book = db.get_book_by_id(book_id)
            if not book:
                raise ResourceNotFound(resource_type="Book", field="id", value=book_id)
            book = book.serialize()
        return book

    def edit_book(self, book_id, new_book):
        db = SQLiteDatabaseConnection()
        existing_book = self.get_book(book_id)
        if not existing_book:
            raise ResourceNotFound(resource_type="Book", field="id", value=book_id)
        new_book_model = BooksDBModel(id=book_id, **new_book)
        with db:
            existing_book = db.get_book_by_author_and_name(name=new_book_model.name, author=new_book_model.author)
            if existing_book:
                raise BookAlreadyExists(new_book)
            rows = db.update_book(book_id, new_book_model)
            if rows == 0:
                raise Exception
        return self.get_book(book_id)

    def delete_book(self, book_id):
        db = SQLiteDatabaseConnection()
        with db:
            rows = db.delete_book_by_id(book_id)
        if rows == 0:
            raise ResourceNotFound(resource_type="Book", field="id", value=book_id)


