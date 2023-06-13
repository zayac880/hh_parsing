from spj.vacancy_spj import Vacancy_spj


def get_vacancies_spj(spj_api, keyword, count):
    """
    Получает и возвращает список вакансий по ключевым словам.
    """
    vacancies = spj_api.get_request(keyword, count)
    return [
        Vacancy_spj(
            profession=item['profession'],
            payment_from=item['payment_from'],
            candidat=item['candidat'],
            link=item['link']
        ) for item in vacancies
    ]
