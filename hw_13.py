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
    txt_handler = txt_handler.read()
    print("Содержимое TXT:\n", txt_handler)


class CSVHandler:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def read(self) -> List[dict]:
        """Читает CSV файл и возвращает список словарей."""
        try:
            with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                return list(reader)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.file_path} не найден")
        except PermissionError:
            raise PermissionError(f"Нет прав на чтение файла {self.file_path}")
    def write(self, data: List[dict]) -> None:
        """Записывает данные в CSV файл."""
        try:
            with open(self.filepath, 'w', newline='', encoding='utf-8') as csvfile:
                if not data:
                    return
                fieldnames = data[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.filepath} не найден")
        except PermissionError:
            raise PermissionError(f"Нет прав на запись в файл {self.filepath}")
    def append(self, data: List[dict]) -> None:
        """Добавляет данные в CSV файл."""
        try:
            with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
                if not data:
                    return
                fieldnames = data[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.filepath} не найден")
        except PermissionError:
            raise PermissionError(f"Нет прав на запись в файл {self.filepath}")
            
if __name__ == '__main__':
    csv_handler = CSVHandler('test.csv')
    data_csv = [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]
    csv_handler.write(data_csv)
    csv_handler.append([{'name': 'Charlie', 'age': '35'}])
    content_csv = csv_handler.read()
    print("Содержимое CSV:\n", content_csv)