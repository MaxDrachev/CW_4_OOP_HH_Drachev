from data.class_HH import HHApi
from data.class_Vacancy import Vacancy
from data.JSON_saver import JSONSaver


def get_vacancies_by_salary(vacancies_data: list, salary_range: str):
    """
    сортировка вакансий по валидному интервалу зарплат.
    """
    min_salary, max_salary = map(int, salary_range.split('-'))
    ranged_vacancies = []
    for vacancy in vacancies_data:
        if vacancy.salary_from is not None and vacancy.salary_to is not None:
            if vacancy.salary_from >= min_salary and vacancy.salary_to <= max_salary:
                ranged_vacancies.append(vacancy)
    return ranged_vacancies


def sort_vacancies(vacancies_data: list):
    """
    сортировка по ключу зп от большего к меньшему.
    """
    return sorted(vacancies_data, key=lambda x: x.salary_from, reverse=True)


def get_filtered_vacancies(vacancies, filter_words):
    """
    фильтрация по ключивым словам (город)
    """
    filtered_by_keywords = []
    for vacancy in vacancies:
        if vacancy.area in filter_words:
            filtered_by_keywords.append(vacancy)
    return filtered_by_keywords


def get_top_vacancies(vacancies_data: list, top_n):
    """
    функция фозвращает топ вакансий.
    """
    return vacancies_data[:top_n]


def user_interaction():
    """
    функция основной логики
    """
    search_query = input("Введите ваш запрос (например Python): ")

    hh_api = HHApi()
    vacancies_from_hh = hh_api.get_vacancies(search_query)
    vacancies_list = [Vacancy.from_json(vacancy) for vacancy in vacancies_from_hh]

    salary_range = input("Введите зарплату (Пример: 50000 - 350000): ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    city_for_filter = input("Введите город: ").split()
    filtered_vacancies_by_city = get_filtered_vacancies(vacancies_list, city_for_filter)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies_by_city, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)

    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    data_manager = JSONSaver()
    data_manager.dump_to_file(vacancies_list)

    for i in top_vacancies:
        print(i)
