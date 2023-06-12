import json
import os


class JSONSaver:
    """
    Класс JSONSaver используется для сохранения и загрузки вакансий в JSON-файл.
    """
    def __init__(self, filename):
        """
        Инициализация объекта JSONSaver.
        :param filename: Имя файла для сохранения и загрузки данных.
        """
        self.filename = filename

    def insert(self, vacancy):
        """
        Вставляет вакансию в JSON-файл
         :param vacancy: Вакансия для сохранения.
        """
        file_data = self.load_all()
        file_data.append(vacancy.to_dict())
        self.save_data(file_data)

    def load_all(self):
        """
        Загружает все вакансии из JSON-файла.
        :return: Список вакансий.
        """
        if not os.path.isfile(self.filename):
            return []
        with open(self.filename, 'r', encoding='utf-8') as f:
            try:
                file_data = json.load(f)
            except json.JSONDecodeError:
                file_data = []
        return file_data

    def delete(self, number):
        """
        Удаляет вакансию из JSON-файла по номеру.
        :param number: Номер вакансии для удаления.
        :return: True, если удаление выполнено успешно, False в противном случае.
        """
        file_data = self.load_all()
        if 0 <= number < len(file_data):
            del file_data[number]
            self.save_data(file_data)
            return True
        return False

    def save_data(self, data):
        """
        Сохраняет данные в JSON-файл.
        :param data: Данные для сохранения.
        """
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f)
