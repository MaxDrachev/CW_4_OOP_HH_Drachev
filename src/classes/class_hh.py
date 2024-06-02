import requests
from abc import ABC, abstractmethod


class Parser(ABC):

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HHApi(Parser):
    """
    Класс для работы с API HeadHunter
    """
    url: str
    headers: dict
    __params: dict
    vacancies: list

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'area': '113', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def get_vacancies(self, keyword: str) -> list:
        """
        Функция получения списка вакансий с api hh, по основному параметру 'text'
        """
        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.__params)
            if response.status_code != 200:
                print(f"Ошибка запроса к API: Статус {response.status_code}")
                break
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.__params['page'] += 1

        return self.vacancies
