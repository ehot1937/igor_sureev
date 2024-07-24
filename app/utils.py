import re
from app.settings import settings

"""
Файл содержит функции валидаторы данных, которые вводит пользователь.

"""


def print_all_commands(commands_str: str = settings.app_commands):
    print(commands_str)
    print("При вводе команд соблюдайте регистр(строчные/заглавные буквы.")


def validate_title() -> str:
    while True:
        title = input("Введите название(title): ")
        if title.isalpha():
            return title
        else:
            print("Название должно содержать только буквы.\n")


def validate_author() -> str:
    while True:
        author = input("Введите автора(author): ")
        if author.isalpha():
            return author

        else:
            print("Название должно содержать только буквы.\n")


def validate_id() -> str:
    pattern = re.compile(
        r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}",
        re.IGNORECASE,
    )

    while True:
        book_id = input("Введите id книги: ")
        if pattern.match(book_id):
            return book_id
        else:
            print("Введите корректный id")


def validate_year() -> str:
    while True:
        year = input("Введите год в формате YYYY: ")
        if year.isdigit() and len(year) == 4:
            return year
        else:
            print("Год состоит из 4х цифр, например 1980")


def status_validate() -> str:
    print(f"Доступные статусы {*settings.status_list,}\n")
    while True:
        new_status = input("Введите новый status книги: ")

        if new_status in settings.status_list:
            return new_status
        else:
            print("Вы ввели недопустимый status.")
