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
    txt_handler.write("Привет, мир!\n")
    txt_handler.append(f"Пока, мир!")
    txt_handler = txt_handler.read()
    print("Содержимое TXT:\n", txt_handler)


class CSVFileHandler:
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
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.file_path} не найден")
        except PermissionError:
            raise PermissionError(f"Нет прав на чтение файла {self.file_path}")
    def write(self, data: List[dict]) -> None:
        """
        Записывает данные в файл
        :param data: данные для записи
        :raise PermissionError: если нет прав на запись в файл
        """
        try:
            with open(self.file_path, "w", newline="", encoding="utf-8") as file:
                fieldnames = data[0].keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
        except PermissionError:
            raise PermissionError(f"Нет прав на запись в файл {self.file_path}")
    def append(self, data: List[dict]) -> None:
        """
        Добавляет данные в файл
        :param data: данные для записи
        :raise PermissionError: если нет прав на запись в файл
        """
        try:
            with open(self.file_path, "a", newline="", encoding="utf-8") as file:
                fieldnames = data[0].keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerows(data)
        except PermissionError:
            raise PermissionError(f"Нет прав на запись в файл {self.file_path}")
        
if __name__ == "__main__":
    csv_handler = CSVFileHandler('test.csv')
    data_csv = [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]
    csv_handler.write(data_csv)
    csv_handler.append([{'name': 'Charlie', 'age': '35'}])
    content_csv = csv_handler.read()
    print("Содержимое CSV:\n", content_csv)


class JSONFileHandler:
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
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {self.file_path} не найден")
        except PermissionError:
            raise PermissionError(f"Нет прав на чтение файла {self.file_path}")
    def write(self, data: List[dict]) -> None:
        """
        Записывает данные в файл
        :param data: данные для записи
        :raise PermissionError: если нет прав на запись в файл
        """
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except PermissionError:
            raise PermissionError(f"Нет прав на запись в файл {self.file_path}")
    def append(self, data: List[dict]) -> None:
        """
        Добавляет данные в файл
        :param data: данные для записи
        :raise FileNotFoundError если файл не найден
        :raise PermissionError: если нет прав на запись в файл\
        """
        try:
            # чтение
            current_data = self.read()
            # объединение данных
            current_data.extend(data)
            # перезапись
            self.write(current_data)
        except FileNotFoundError:
            # если файла нет - созданеи и внесение в него данных
            self.write(data)
        except PermissionError:
            raise PermissionError(f"Нет прав на запись в файл {self.file_path}")
        
if __name__ == "__main__":
    json_handler = JSONFileHandler("test.json")
    data_json = [{'product': 'Laptop', 'price': 1500}, {'product': 'Phone', 'price': 800}]
    json_handler.write(data_json)
    json_handler.append([{'product': 'Tablet', 'price': 600}])
    content_json = json_handler.read()
    print("Содержимое JSON:\n", content_json)