

class Vacancy:
    """
    Инициализация вакансии с заданными атрибутами
    """

    title: str  # Название вакансии
    url: str  # URL страницы вакансии
    salary: int  # Зарплата предложенная за работу
    schedule: str  # требования по графику

    def __init__(self, title, url, salary, schedule):
        self.title = title
        self.url = url
        self.schedule = schedule
        self.salary = salary

    def __str__(self):
        """
        Строковое представление объекта
        """
        return f'\n{self.title}\t{self.schedule}\t{self.salary}'

    def __repr__(self):
        """
        Официальное строковое представление объекта
        """
        return f'\n{self.title}\t{self.schedule}\t{self.salary}'

    def __gt__(self, other):
        """"
        Определение поведения для оператора '>'. Сравнивает вакансии по зарплате
        """
        return self.salary > other.salary

    def to_json(self):
        """
         Конвертирует объект вакансии в JSON-формат.
        """
        return {
            'title': self.title,
            'url': self.url,
            'schedule': self.schedule,
            'salary': self.salary
        }
