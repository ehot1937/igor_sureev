from app.db_connector.book_connector import BookConnector
from app.settings import settings

book_connector = BookConnector()


def get_book() -> list[dict] | str:
    """
    Функция отвечает за поиск книги по заданным пользователем фильтрам, валидацию вводимых пользователем данных.
    :returns
        list[dict] - список объектов из бд
        str - Сообщение об отсутствии записи или подключения к бд
    """
    print(f"Доступные фильтры для поиска: {*settings.filters,}.\n")

    while True:
        client_filter = input("Введите название фильтра: ")
        if client_filter in settings.filters:
            break
        else:
            print("Вы ввели неверное название фильтра, попробуйте еще раз.\n")

    if client_filter == "title":
        request = input("Введите название(title) искомой книги: \n")
        response = book_connector.get(title=request)
        return response

    if client_filter == "author":
        request = input("Введите автора(author) искомой книги: \n")
        response = book_connector.get(author=request)
        return response

    if client_filter == "year":
        request = input("Введите год печати(year) искомой книги: \n")
        response = book_connector.get(year=request)
        return response

    return "По вашему запросу ничего не найдено"
