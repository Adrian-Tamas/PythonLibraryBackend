import json
from functools import wraps

from library_backend.exception import InvalidUser, InvalidBook
from library_backend.service import UserService


def response(message, status_code):
    return {
        'status_code': str(status_code),
        'body': json.dumps(message)
    }


def handle_request():
    """
    Handle common exceptions.
    :return: Decorated function.
    """

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return response(f(*args, *kwargs), 200)
            except (InvalidUser, InvalidBook, ValueError) as e:
                return response(str(e), 400)
            except KeyError as e:
                return response(f'{str(e)} is required', 400)

        return wrapper

    return decorator


class UserApi:

    @handle_request()
    def create_user(self, user):
        if user["a"] == "a":
            raise InvalidUser("user with a in value")
        userService = UserService()
        userService.create_user(user=user)
        return user

    @handle_request()
    def list_users(self):
        return [{"my_user": "user"}]

    @handle_request()
    def delete_user(self, user_id):
        return f"succesfully deleted user {user_id}"

    @handle_request()
    def update_user(self, user_id, new_user):
        new_user["my_new_el"] = "new"
        return new_user

    @handle_request()
    def get_user(self, user_id):
        return {"my_user": "user"}


class BookApi:

    @handle_request()
    def get_books(self):
        return [{"My_books": "books"}]

    @handle_request()
    def create_book(self, book):
        return {"new_book": book}

    @handle_request()
    def get_book(self, book_id):
        return {"one_book": book_id}

    @handle_request()
    def update_book(self, book_id, new_book):
        new_book["new_field"] = "new"
        return new_book

    @handle_request()
    def delete_book(self, book_id):
        return f"Book with id {book_id} has been deleted"


class ReservationApi:

    @handle_request()
    def get_reservations(self):
        return [{"user_id": "3", "book_id": "5"}]

    @handle_request()
    def add_reservation(self, reservation):
        return {"reservation": reservation}

    @handle_request()
    def get_reservation_by_user_id(self, user_id):
        return {"user_id": user_id, "reservation": "1"}

    @handle_request()
    def get_reservation_by_book_id(self, book_id):
        return {"book_id": book_id, "reservation": "1"}

    @handle_request()
    def update_reservation(self, user_id, book_id):
        return {"user_id": user_id, "book_id": book_id}

    @handle_request()
    def delete_reservation(self, user_id, book_id):
        return f"Reservation was deleted for {user_id} and {book_id}"

    @handle_request()
    def delete_all_reservations_for_users(self, user_id):
        return f"all reservations were deleted for user: {user_id}"

    @handle_request()
    def delete_all_reservations_for_book(self, book_id):
        return f"all reservations were deleted for book: {book_id}"
