import logging

from flask import Flask, Response, request

from library_backend.api import UserApi, BookApi
from library_backend.database import SQLiteDatabaseConnection

# logger = logging.getLogger(__name__)

app = Flask("LibraryBackend")

CONTENT_TYPE = "application/json"


def app_response(api_response):
    return Response(response=api_response['body'], status=api_response['status_code'], content_type=CONTENT_TYPE)


@app.route('/users', methods=['POST'])
def create_user():
    user = request.get_json()
    user_api = UserApi()
    response = user_api.create_user(user)
    return app_response(response)


@app.route('/users', methods=['GET'])
def list_users():
    user_api = UserApi()
    response = user_api.list_users()
    return app_response(response)


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_api = UserApi()
    response = user_api.delete_user(user_id)
    return app_response(response)


@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    new_user = request.get_json()
    user_api = UserApi()
    response = user_api.update_user(user_id, new_user)
    return app_response(response)


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user_api = UserApi()
    response = user_api.get_user(user_id)
    return app_response(response)


@app.route('/books', methods=['GET'])
def get_books():
    book_api = BookApi()
    response = book_api.get_books()
    return app_response(response)


@app.route('/books', methods=['POST'])
def create_book():
    book = request.get_json()
    book_api = BookApi()
    response = book_api.create_book(book)
    return app_response(response)


@app.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    book_api = BookApi()
    response = book_api.get_book(book_id)
    return app_response(response)


@app.route('/books/<book_id>', methods=['PUT'])
def edit_book(book_id):
    new_book = request.get_json()
    book_api = BookApi()
    response = book_api.update_book(book_id, new_book)
    return app_response(response)


@app.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    book_api = BookApi()
    response = book_api.delete_book(book_id)
    return app_response(response)


if __name__ == '__main__':
    db = SQLiteDatabaseConnection()
    with db:
        db.create_tables_if_not_exists()
    with db:
        db.add_some_data_if_does_not_exist()
    app.run(host="127.0.0.1", port=50000, debug="True")
