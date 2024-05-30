class Vacancy:

    def __init__(self, name, url, description, area, salary_from, salary_to, currency):
        """
        Инициализация объекта вакансия.
        """
        self.name = name
        self.url = url
        self.description = description
        self.area = area
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency

    def __str__(self):
        """
        Вывод информации об объекте.
        """
        return f'Вакансия: {self.name}\n' \
               f'Город: {self.area}\n' \
               f'Требования: {self.description}\n' \
               f'Зарплата от {self.salary_from} до {self.salary_to} {self.currency}\n'

    @staticmethod
    def from_json(json_item):
        """
        Создание объекта из полученого JSON словаря.
        """
        area_info = json_item.get('area')
        area = area_info['name'] if area_info and 'name' in area_info else None
        salary_info = json_item.get('salary')
        salary_from = salary_info['from'] if salary_info and 'from' in salary_info else 0
        salary_to = salary_info['to'] if salary_info and 'to' in salary_info else 0
        currency = salary_info['currency'] if salary_info and 'currency' in salary_info else None

        return Vacancy(
            name=json_item['name'],
            url=json_item['alternate_url'],
            description=json_item['snippet']['requirement'],
            area=area,
            salary_from=salary_from,
            salary_to=salary_to,
            currency=currency
        )

    def to_dict(self):
        """
        Конвертация объекта в словарь
        """
        return {
            'name': self.name,
            'url': self.url,
            'description': self.description,
            'area': self.area,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'currency': self.currency
        }

    @classmethod
    def from_dict(cls, dict_item):
        """
        создание объекта из словаря.
        """
        return cls(**dict_item)

    def __lt__(self, other):
        """Less than operator for comparison based on salary_from."""
        return self.salary_from < other.salary_from

    def __le__(self, other):
        """Less than or equal to operator for comparison based on salary_from."""
        return self.salary_from <= other.salary_from

    def __eq__(self, other):
        """Equality operator for comparison based on salary_from."""
        return self.salary_from == other.salary_from

    def __ne__(self, other):
        """Not equal operator for comparison based on salary_from."""
        return self.salary_from != other.salary_from

    def __gt__(self, other):
        """Greater than operator for comparison based on salary_from."""
        return self.salary_from > other.salary_from

    def __ge__(self, other):
        """Greater than or equal to operator for comparison based on salary_from."""
        return self.salary_from >= other.salary_from
