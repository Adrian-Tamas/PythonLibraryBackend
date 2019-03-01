from library_backend.database import SQLiteDatabaseConnection
from library_backend.models.database.books_db_model import BooksDBModel
from library_backend.models.database.users_db_model import UsersDBModel

db = SQLiteDatabaseConnection()
with db:
    # user1 = UsersDBModel(user_email="adrian.tamas@endava.com", user_first_name="Adrian", user_last_name="Tamas")
    # db.add_user(user1)

    users = db.get_all_users()
    print(f"All users: {users}")

    users1 = db.get_users_by_first_and_last_name(first_name="Adrian", last_name="Tamas")
    print(f"List of users by name {users1}")

    users2 = db.get_users_by_first_and_last_name(first_name="Adriana", last_name="Tamas")
    print(f"List non existing users {users2}")

    user = db.get_user_by_email(email="adi.tamas@endava.com")
    print(f"get user by email {user}")

    # book2 = BooksDBModel(book_name="Nightflyers", book_author="George R.R. Martin")
    # db.add_book(book2)

    all_books = db.get_all_books()
    print(f"All Books {all_books}")

    book_by_name = db.get_books_by_name("Nightflyers")
    print(f"Book by exact name {book_by_name}")

    book_by_author = db.get_books_by_author("George R.R. Martin")
    print(f"Book by exact author name {book_by_author}")

    book_by_name_and_author = db.get_book_by_author_and_name(name="Nightflyers",
                                                             author="George R.R. Martin")
    print(f"Book by name and author: {book_by_name_and_author}")

    book_by_partial_name = db.get_books_by_partial_author_name("R.R.")
    print(f"Book by partial name {book_by_partial_name}")

    db.get_reserved_books()
