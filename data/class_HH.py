import requests
from abc import ABC
from data.class_Vacancy import Vacancy


class Parser(ABC):

    def load_vacancies(self, keyword):
        pass


class HH_API(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'area': '113', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def get_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            if response.status_code != 200:
                print(f"Ошибка запроса к API: Статус {response.status_code}")
                break
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

        vacancies_objects = []
        for item in self.vacancies:
            vacancies_objects.append(
                Vacancy(
                    title=item.get('name'),
                    url=item.get('alternate_url'),
                    schedule=item.get('schedule').get('name'),
                    salary=(item.get('salary')
                            )
                )
            )
        return vacancies_objects


if __name__ == '__main__':
    hh_1 = HH_API()
    vac_hh_1 = hh_1.get_vacancies('python')
    print(vac_hh_1[0:5])
