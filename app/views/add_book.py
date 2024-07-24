from app.db_connector.book_connector import BookConnector
from app.utils import validate_year, validate_title, validate_author

book_connector = BookConnector()


def add_book() -> str:
    """
    Функция отвечает за добавление новой книги, формирует объект(в данном случае dict)
     и передает его в коннектор для записи в базу данных.
    """
    title = validate_title()
    author = validate_author()
    year = validate_year()

    new_book = {
        "title": title,
        "author": author,
        "year": year,
    }
    response = book_connector.save(new_book)

    return response
