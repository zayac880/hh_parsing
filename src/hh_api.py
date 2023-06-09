from abc import ABC, abstractmethod
import requests


class VacancyAPI(ABC):
    @abstractmethod
    def get_request(self, keyword, count):
        pass


class HH(VacancyAPI):
    def get_request(self, keyword, count):
        pages = int(count / 1)
        params = {
            "keyword": keyword,
            "page": 0,
            "per_page": 1
        }
        response = []
        for page in range(pages):
            params.update({"page": page})
            data = requests.get(f'https://api.hh.ru/vacancies', params=params)
            response += data.json()['items']

        return response
