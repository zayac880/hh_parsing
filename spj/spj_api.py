import os
import requests
from dotenv import load_dotenv
from abc import ABC, abstractmethod

load_dotenv()


class SuperJobApi(ABC):
    """
    Абстрактный метод для получения данных о вакансиях.
    keyword (str): Ключевое слово для поиска вакансий.
    count (int): Количество вакансий, которое нужно получить.
    """
    @abstractmethod
    def get_request(self, keyword, count):
        pass


class SPJ(SuperJobApi):
    """
    Класс для получения данных о вакансиях через API(SPJ).
    keyword (str): Ключевое слово для поиска вакансий.
    count (int): Количество вакансий, которое нужно получить.
    """
    def __init__(self):
        """
        Инициализация объекта SPJ.
        """
        self.api_key = os.getenv("API_KEY_SPJ")

    def get_request(self, keyword, count):
        items_per_page = 100
        pages = (count - 1) // items_per_page + 1
        response_data = []
        for page in range(pages):
            params = {
                "keyword": keyword,
                "count": items_per_page,
                "page": page + 1
            }
            headers = {
                "X-Api-App-Id": self.api_key
            }
            response = requests.get("https://api.superjob.ru/2.0/vacancies", params=params, headers=headers)
            data = response.json()
            if "objects" in data:
                response_data += data["objects"]
            # Проверяем, достаточно ли уже получено вакансий
            if len(response_data) >= count:
                response_data = response_data[:count]
                break

        return response_data
