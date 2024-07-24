from app.db_connector.book_connector import BookConnector
from app.utils import validate_id, status_validate

book_connector = BookConnector()


def change_book_status() -> str:
    """
    Функция отвечает за изменение статуса книги.
    После проверки наличия книги вызывает метод коннектора.
    :return:
        Str - Сообщение об изменении статуса книги или ошибке
    """

    book_id = validate_id()

    new_status = status_validate()

    book = book_connector.get(id=book_id)

    if not book:
        return "Книги с таким id не найдено."

    response = book_connector.update(book[0]["id"], new_status)

    return response
