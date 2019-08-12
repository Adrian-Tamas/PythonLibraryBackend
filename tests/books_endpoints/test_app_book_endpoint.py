import json

from unittest.mock import patch

import app


class TestLibraryBackendAppBookEndpoints:

    def test_book_create_valid(self, mock_book_payload, mock_book_resource):
        with patch('library_backend.service.BookService.create_book') as test_mock:
            test_mock.return_value = mock_book_resource
            with app.app.test_request_context('/books', method="POST",
                                              json=mock_book_payload):
                response = app.create_book()
            assert '200' == response.status
            assert mock_book_resource == json.loads(response.get_data().decode('utf-8'))
