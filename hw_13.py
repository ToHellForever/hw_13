"""
hw_13: В данном задании вам необходимо реализовать три класса для работы с файлами: `TxtFileHandler`, `CSVFileHandler` и `JSONFileHandler`. Каждый класс должен обеспечивать чтение, запись и добавление данных в соответствующий формат файлов. При этом классы для CSV и JSON должны работать со списками словарей. Особое внимание уделите реализации метода добавления (APPEND) для JSON, чтобы корректно объединять новые данные с уже существующими в файле.
"""

from typing import *
import json
import csv


# Работа с txt файлом
class TxtHandler:
    """
    Класс для работы с текстовыми файлами
    Methods:
        - read() -> List[str] - возвращает список строк из файла
        - write(*data: str) -> None - записывает данные в файл
        - append(*data: str) -> None - добавляет данные в файл
    Exceptions:
        - FileNotFoundError: если файл не найден
        - PermissionError: если нет прав на запись в файл
    """

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read(self) -> List[str]:
        """
        Читает данные из файла и возвращает список строк
        :return: список строк
        :raise FileNotFoundError: если файл не найден
        :raise PermissionError: если нет прав на чтение файла
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return file.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.file_path} не найден")
        except PermissionError:
            raise PermissionError(f"Нет прав на чтение файла {self.file_path}")

    def write(self, *data: str) -> None:
        """
        Записывает данные в файл
        :param data: данные для записи
        :raise PermissionError: если нет прав на запись в файл
        """
        prepared_data = [line + "\n" for line in data]
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                file.writelines(data)
        except PermissionError:
            raise PermissionError(f"Нет прав на запись в файл {self.file_path}")

    def append(self, *data: str) -> None:
        """
        Добавляет данные в файл
        :param data: данные для записи
        :raise PermissionError: если нет прав на запись в файл
        """
        try:
            with open(self.file_path, "a", encoding="utf-8") as file:
                file.writelines(data)
        except PermissionError:
            raise PermissionError(f"Нет прав на запись в файл {self.file_path}")


if __name__ == "__main__":
    txt_handler = TxtHandler("test.txt")
    txt_handler.write("Привет, мир!")
    txt_handler.append("Пока, мир!")
    print(txt_handler.read())


# Работа с csv файлом
class CSVHandler:
    """
    Класс для работы с csv файлами
    Methods:
        - read() -> List[List[dict]] - возвращает список словарей из файла
        - write(*data: List[dict]) -> None - записывает список словарей в CSV файл
        - append(*data: List[dict]) -> None - добавляет список словарей в конец CSV файла
    """

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read(self) -> List[dict]:
        """
        Читает данные из файла и возвращает список словарей
        :return: список словарей
        :raise FileNotFoundError: если файл не найден
        :raise PermissionError: если нет прав на чтение файла
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                reader = file.DictReader(file)
                return reader
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.file_path} не найден")
        except PermissionError:
            raise PermissionError(f"Нет прав на чтение файла {self.file_path}")
