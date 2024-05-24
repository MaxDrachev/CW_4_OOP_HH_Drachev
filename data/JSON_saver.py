import json
import os
from data.class_HH import HH_API
from config import ROOT_DIR


class JSONSaver:
    """
    Класс для сохранения данных о вакансиях в формате JSON в файл.

    Методы:
      dump_to_file(vacancies, filename, directory): Сохраняет список вакансий в файл JSON.
        Принимает список вакансий, имя файла и директорию для сохранения.
    """

    def dump_to_file(self, vacancies_objects, filename="vacancies.json"):
        if not isinstance(vacancies_objects, list):
            raise ValueError("Ожидается, что объект vacancies является списком.")

        full_path = os.path.join(ROOT_DIR, filename)  # Путь к файлу

        try:
            vacancies_file = [vac.to_json() for vac in vacancies_objects]
            with open(full_path, 'w', encoding='UTF-8') as file:
                json.dump(vacancies_file, file, ensure_ascii=False, indent=4)
            print(f"Данные успешно сохранены в {full_path}")
        except AttributeError:
            raise ValueError("Убедитесь, что каждый элемент vacancies имеет метод to_json.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    vac = HH_API().get_vacancies("python")
    JSONSaver().dump_to_file(vac)
