from unittest import mock

import pytest


@pytest.fixture()
def mock_user_payload():
    yield {
        "first_name": "John",
        "last_name": "Smith",
        "email": "jhonsmith@email.com"
    }


@pytest.fixture()
def mock_user_resource():
    yield {
        "id": "123",
        "first_name": "John",
        "last_name": "Smith",
        "email": "jhonsmith@email.com"
    }


@pytest.fixture()
def mock_users_resource():
    yield [{
        "id": "123",
        "first_name": "John",
        "last_name": "Smith",
        "email": "jhonsmith@email.com"
    }, {
        "id": "124",
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "janesmith@email.com"
    }
    ]


@pytest.fixture()
def mock_book_payload():
    yield {
        "name": "My test book",
        "author": "Unknown Author",
        "description": "A test book created for unit tests",
        "cover": "https://test.com/cover.jpg"
    }


@pytest.fixture()
def mock_book_resource():
    yield {
        "id": "123",
        "name": "My test book",
        "author": "Unknown Author",
        "description": "A test book created for unit tests",
        "cover": "https://test.com/cover.jpg"
    }


@pytest.fixture()
def mock_db_session():
    with mock.patch('library_backend.database.create_engine'):
        with mock.patch('library_backend.database.sessionmaker') as sessionmaker_mock:
            session = sessionmaker_mock()()
            yield session
