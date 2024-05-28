from data.class_HH import HHApi
from data import class_Vacancy


def get_vacancies_by_salary(vacancies_data: list, salary_range: str):
    """
    Filters vacancies within a specified salary range.

    :param vacancies_data: List of Vacancy objects to filter.
    :param salary_range: String specifying the minimum and maximum salary values.

    :return: Filtered list of Vacancy objects within the salary range.
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
    Sorts a list of vacancies by their starting salary in descending order.

    :param vacancies_data: List of Vacancy objects to sort.

    :return: Sorted list of Vacancy objects.
    """
    return sorted(vacancies_data, key=lambda x: x.salary_from, reverse=True)


def get_top_vacancies(vacancies_data: list, top_n):
    """
    Returns the top N vacancies from a sorted list.

    :param vacancies_data: Sorted list of Vacancy objects.
    :param top_n: Number of top vacancies to return.

    :return: Top N Vacancy objects.
    """
    return vacancies_data[:top_n]


def user_interaction():
    """
    Interacts with the user to perform operations on job vacancies fetched from HeadHunter.

    Prompts the user for a search query, saves the fetched vacancies, and displays the top vacancies based on user-defined criteria.
    """
    search_query = input("Введите ваш запрос (например Python): ")
    hh_api = HHApi()

    vacancies_list = hh_api.get_vacancies(search_query)
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    vacancies_by_city = input("Введите город: ").split()
    salary_range = input("Введите диапазон зарплат: ")

    data_manager = DataManager()
    data_manager.save_vacancies(vacancies_list)

    salary_range = input("Введите зарплату (Пример: 50000 - 350000): ")

    ranged_vacancies = get_vacancies_by_salary(vacancies_list, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_n = len(sorted_vacancies)  # Показываем все найденные вакансии, соответствующие критериям
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    for i in top_vacancies:
        print(i)
