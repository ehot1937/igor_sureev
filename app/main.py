from app.views.add_book import add_book
from app.views.get_all_books import get_all_books
from app.views.delete_book import delete_book
from app.views.get_book import get_book
from app.views.change_book_status import change_book_status
from app.utils import print_all_commands
from app.db_connector.book_connector import ensure_file_exists


def main():
    """
    Функция обрабатывает основные консольные команды.
    """
    commands = {
        "1": add_book,
        "2": delete_book,
        "3": get_book,
        "4": get_all_books,
        "5": change_book_status,
    }
    while True:
        incoming_command = input(
            "Введите номер действия или команду stop для выхода из программы\n" "Ввод: "
        )
        if incoming_command == "stop":
            break

        if incoming_command == "menu":
            print_all_commands()

        command_function = commands.get(incoming_command)
        if command_function:
            result = command_function()
            print(result)


if __name__ == "__main__":
    print_all_commands()
    ensure_file_exists()
    main()
