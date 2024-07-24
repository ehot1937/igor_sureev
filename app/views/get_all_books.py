from app.db_connector.book_connector import BookConnector

book_connector = BookConnector()


def get_all_books() -> list[dict] | str:
    return book_connector.get()
