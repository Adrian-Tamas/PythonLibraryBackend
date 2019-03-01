from flask import Flask

from library_backend.database import SQLiteDatabaseConnection

app = Flask("LibraryBackend")


if __name__ == '__main__':

    db = SQLiteDatabaseConnection()
    with db:
        db.create_tables_if_not_exists()

    with db:
        db.add_some_data_if_does_not_exist()

    app.run(debug="True")
