from hh.vacancy import Vacancy


def get_vacancies(hh_api, keyword, count):
    """
    Получает и возвращает список вакансий по ключевым словам.
    """
    vacancies = hh_api.get_request(keyword, count)
    return [
        Vacancy(
            name=item['name'],
            salary=item['salary']['to'] if item['salary'] else None,
            description=item['snippet']['responsibility'],
            link=item['alternate_url']
        ) for item in vacancies
    ]


def save_vacancies(vacancy_saver, vacancies):
    """
    Сохраняет выбранную вакансию в JSON.
    """
    number = int(input("Введите номер вакансии для сохранения: "))
    if number < 1 or number > len(vacancies):
        print("Некорректный номер вакансии.")
    else:
        vacancy = vacancies[number - 1]
        vacancy_saver.insert(vacancy)  # Сохраняем выбранную вакансию в JSON файл


def show_saved_vacancies(vacancy_saver):
    """
    Показывает сохраненные вакансии.
    """
    print("Сохраненные вакансии:")
    saved_vacancies = vacancy_saver.load_all()
    if not saved_vacancies:
        print("Нет сохраненных вакансий.")
    else:
        for number, vacancy_data in enumerate(saved_vacancies, start=1):
            vacancy = Vacancy(
                name=vacancy_data['name'],
                salary=vacancy_data['salary'],
                description=vacancy_data['description'],
                link=vacancy_data['link']
            )
            print(f"Вакансия #{number}:")
            print(vacancy)
            print("--------------------")
        delete_number = int(input("Введите номер вакансии для удаления (или 0 для отмены): "))
        if delete_number == 0:
            return
        elif delete_number < 1 or delete_number > len(saved_vacancies):
            print("Некорректный номер вакансии.")
        else:
            vacancy_saver.delete(delete_number - 1)  # Удаляем выбранную вакансию из JSON файла
            print("Вакансия удалена.")
