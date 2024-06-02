import json
import os
from abc import ABC, abstractmethod
from src.classes.class_vacancy import Vacancy

from data.config import ROOT_DIR


class AbstractJSONSaver(ABC):
    """
    абстрактный класс, с 3 методами, запись чтение и удаление из файла
    """

    @abstractmethod
    def dump_to_file(self, vacancies_from_api: list):
        pass

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def delite_from_file(self):
        pass


class JSONSaver(AbstractJSONSaver):
    """
    Класс для сохранения, чтения и удаления данных о вакансиях в формате JSON.
    """
    filename: str
    full_path: str

    def __init__(self):
        self.filename = filename = "vacancies.json"
        self.full_path = os.path.join(ROOT_DIR, filename)

    def dump_to_file(self, vacancies_objects: list):
        """
        Запись данных с api hh в файл
        """
        with open(self.full_path, 'w', encoding='UTF-8') as file:
            json.dump(vacancies_objects, file, ensure_ascii=False, indent=4)

    def delite_from_file(self):
        """
        Удаление данных с файла
        """
        f = open(self.full_path, "w+")
        f.seek(0)
        f.close()

    def read_file(self) -> list:
        """
        Чтение данных с файла
        """
        with open(self.full_path, encoding='UTF-8') as file:
            return json.load(file)

    def load_from_file(self):
        with open(self.full_path, 'r', encoding='utf-8', errors='replace') as file:
            load_to_user = [Vacancy.from_dict(item) for item in json.load(file)]
            for i in load_to_user:
                print(i)
