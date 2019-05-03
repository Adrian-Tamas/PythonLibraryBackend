import json
from functools import wraps

from library_backend.exceptions import *
from library_backend.service import UserService, BookService
from library_backend.validators import validate_request_for_user


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
            except (InvalidUser,
                    InvalidBook,
                    ValueError,
                    UserAlreadyExists,
                    ResourceNotFound,
                    BookAlreadyExists) as e:
                return response(str(e), 400)
            except KeyError as e:
                return response(f'{str(e)} is required', 400)

        return wrapper

    return decorator


class UserApi:

    @handle_request()
    @validate_request_for_user
    def create_user(self, user):
        user_service = UserService()
        user = user_service.create_user(user_dict=user)
        return user

    @handle_request()
    def list_users(self):
        user_service = UserService()
        user_list = user_service.list_users()
        return user_list

    @handle_request()
    def delete_user(self, user_id):
        user_service = UserService()
        user_service.delete_user(user_id)
        return f"Successfully deleted user {user_id}"

    @handle_request()
    def update_user(self, user_id, new_user):
        user_service = UserService()
        new_user = user_service.update_user(user_id, new_user)
        return new_user

    @handle_request()
    def get_user(self, user_id):
        user_service = UserService()
        user = user_service.get_user(user_id)
        return user


class BookApi:

    @handle_request()
    def get_books(self):
        book_service = BookService()
        return book_service.list_books()

    @handle_request()
    def create_book(self, book):
        book_service = BookService()
        return book_service.create_book(book)

    @handle_request()
    def get_book(self, book_id):
        book_service = BookService()
        return book_service.get_book(book_id)

    @handle_request()
    def update_book(self, book_id, new_book):
        book_service = BookService()
        return book_service.edit_book(book_id, new_book)

    @handle_request()
    def delete_book(self, book_id):
        book_service = BookService()
        book_service.delete_book(book_id)
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
