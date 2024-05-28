from data.class_HH import HHApi


class Vacancy:
    """
    Represents a job vacancy with details such as name, URL, description, salary range, and currency.

    Includes methods  for comparing Vacancy objects based on their starting salary for sorting purposes.
    """

    def __init__(self, name, url, description, salary_from, salary_to, currency):
        """
        Initializes a new Vacancy object.

        :param name: Name of the job vacancy.
        :param url: URL of the job posting.
        :param description: Description of the job requirements.
        :param salary_from: Starting salary value.
        :param salary_to: Ending salary value.
        :param currency: Currency of the salary.
        """
        self.name = name
        self.url = url
        self.description = description
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency

    def __str__(self):
        """
        Returns a string representation of the Vacancy object.

        :return: Human-readable string representation of the Vacancy.
        """
        return f'Вакансия: {self.name}\n' \
               f'Требования: {self.description}\n' \
               f'Зарплата от {self.salary_from} до {self.salary_to} {self.currency}\n'

    @staticmethod
    def from_json(json_item):
        """
        Creates a Vacancy object from a JSON item.

        :param json_item: JSON item representing a job vacancy.

        :return: Vacancy object initialized with data from the JSON item.
        """
        salary_info = json_item.get('salary')
        salary_from = salary_info['from'] if salary_info and 'from' in salary_info else 0
        salary_to = salary_info['to'] if salary_info and 'to' in salary_info else 0
        currency = salary_info['currency'] if salary_info and 'currency' in salary_info else None

        return Vacancy(
            name=json_item['name'],
            url=json_item['alternate_url'],
            description=json_item['snippet']['requirement'],
            salary_from=salary_from,
            salary_to=salary_to,
            currency=currency
        )

    def to_dict(self):
        """
        Converts the Vacancy object to a dictionary.

        :return: Dictionary representation of the Vacancy object.
        """
        return {
            'name': self.name,
            'url': self.url,
            'description': self.description,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'currency': self.currency
        }

    @classmethod
    def from_dict(cls, dict_item):
        """
        Creates a Vacancy object from a dictionary.

        :param dict_item: Dictionary representing a job vacancy.

        :return: Vacancy object initialized with data from the dictionary.
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
        return self.salary_from!= other.salary_from

    def __gt__(self, other):
        """Greater than operator for comparison based on salary_from."""
        return self.salary_from > other.salary_from

    def __ge__(self, other):
        """Greater than or equal to operator for comparison based on salary_from."""
        return self.salary_from >= other.salary_from


if __name__ == '__main__':
    vac_1 = HHApi()
    vac_json = vac_1.get_vacancies('python')
    vacancies = [Vacancy.from_json(i) for i in vac_json]
    print(vacancies)
