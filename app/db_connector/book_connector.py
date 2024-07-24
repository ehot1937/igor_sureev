import json
from uuid import uuid4
from app.settings import settings


def ensure_file_exists(file_path=settings.file_path):
    """

    Подготавливает файл с данными для работы.
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if not file_path.exists():
        with file_path.open("w") as file:
            json.dump([], file, indent=4)


class BookConnector:
    """
    Класс коннектор, получает валидные данные, обращается к базе данных.
    Обрабатывает ответ базы данных.
    :returns
        list[dict] - список объектов из бд
        str - сообщение об отсутствии записи или подключения к бд
    """

    def __init__(self):
        self.file_path = settings.file_path

    def get(
        self,
        id: str | None = None,
        title: str | None = None,
        author: str | None = None,
        year: str | None = None,
        status: str | None = None,
    ) -> list[dict] | str:
        arguments = {
            "id": id,
            "title": title,
            "author": author,
            "year": year,
            "status": status,
        }

        try:
            with open(self.file_path, "r") as file:
                books = json.load(file)
        except FileNotFoundError:
            return f"Файл {self.file_path} не найден, перезапустите приложение."

        filters = {key: value for key, value in arguments.items() if value is not None}

        if not filters:
            return books

        sorted_books = []
        for key, value in filters.items():
            sorted_books = [book for book in books if book.get(key) == value]
            if not sorted_books:
                return []
        return sorted_books

    def save(self, model_data) -> str:
        model_data["id"] = str(uuid4())
        model_data["status"] = "в наличии"

        try:
            with open(self.file_path, "r") as file:
                books = json.load(file)

        except FileNotFoundError:
            return f"Файл {self.file_path} не найден, перезапустите приложение."

        books.append(model_data)
        with open(self.file_path, "w") as file:
            json.dump(books, file, indent=4)

        return "Книга сохранена"

    def update(self, book_id: str, new_status: str) -> str:
        try:
            with open(self.file_path, "r") as file:
                books = json.load(file)
        except FileNotFoundError:
            return f"Файл {self.file_path} не найден, перезапустите приложение."

        for book in books:
            if book["id"] == book_id:
                book["status"] = new_status

        with open(self.file_path, "w") as file:
            json.dump(books, file, indent=4)

        return "Статус обновлен"

    def delete(self, book_id: str) -> str:
        try:
            with open(self.file_path, "r") as file:
                books = json.load(file)
        except FileNotFoundError:
            return f"Файл {self.file_path} не найден, перезапустите приложение."

        for book in books:
            if book["id"] == book_id:
                books.remove(book)

        with open(self.file_path, "w") as file:
            json.dump(books, file, indent=4)

        return "Книга удалена"
