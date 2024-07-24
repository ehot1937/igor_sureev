import os
from pathlib import Path


class Settings:
    current_dir = os.getcwd()
    file_path = Path(os.path.join(current_dir, "db_connector", "library_database.json"))
    app_commands: str = (
        "1) Добавить\n"
        "2) Удалить\n"
        "3) Найти\n"
        "4) Показать все\n"
        "5) Изменить статус\n"
        "menu - посмотреть список доступных команд\n"
        "stop - выйти из программы\n"
    )
    filters: list[str] = ["title", "author", "year"]
    status_list: list[str] = ["в наличии", "выдана"]



settings = Settings()
