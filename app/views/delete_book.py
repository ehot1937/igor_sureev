from app.utils import validate_id
from app.db_connector.book_connector import BookConnector

book_connector = BookConnector()


def delete_book() -> str:
    """
    Функция отвечает за удаление книги из базы данных.
    После проверки наличия книги в базе данных,
    функция вызывает метод коннектора для удаления из бд.
    """
    book_id = validate_id()
    book = book_connector.get(id=book_id)
    if not book:
        return "Книги с таким id не существует"

    response = book_connector.delete(book_id)
    return response
