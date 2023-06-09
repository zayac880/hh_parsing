import json


class JSONSaver:
    def __init__(self, filename):
        self.__filename = filename

    @property
    def file(self):
        return self.__filename

    @file.setter
    def file(self, name):
        self.__filename = name

    def insert(self, data):
        try:
            with open(self.__filename, 'r', encoding='utf-8') as f:
                file_data = json.load(f)
        except FileNotFoundError:
            file_data = []
        file_data.append(data)
        with open(self.__filename, 'w', encoding='utf-8') as f:
            json.dump(file_data, f)
