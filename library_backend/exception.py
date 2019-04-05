class InvalidUser(Exception):
    def __init__(self, value):
        super().__init__(f"Invalid user {value}")


class InvalidBook(Exception):
    def __init__(self, value):
        super().__init__(f"Invalid book {value}")
