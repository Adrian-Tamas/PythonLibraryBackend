from library_backend.database import SQLiteDatabaseConnection
from library_backend.exceptions import UserAlreadyExists, InvalidUser, ResourceNotFound, InvalidFieldException
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
        old_user = self.get_user(user_id)
        if not old_user["email"] == new_user["email"]:
            raise InvalidFieldException("email")
        db = SQLiteDatabaseConnection()
        user_model = UsersDBModel(id=user_id, **new_user)
        with db:
            rows = db.update_user(user_id, user_model)
        user = self.get_user(user_id)
        if rows == 0:
            raise Exception # TODO: handle email error
        return user


class BookService:
    def create_book(self, book):
        pass
