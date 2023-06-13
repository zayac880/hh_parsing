class Vacancy_spj:
    """
    Класс, представляющий вакансию.
    profession (str): Название вакансии.
    payment_from (int): Зарплата.
    candidat (str): Описание вакансии.
    link (str): Ссылка на вакансию.
    """
    def __init__(self, profession, payment_from, candidat, link):
        """
        Инициализация объекта Vacancy_spj.
        """
        self.profession = profession
        self.payment_from = payment_from
        self.candidat = candidat
        self.link = link

    def __str__(self):
        """
        Возвращает строковое представление объекта Vacancy_spj.
        Строка с названием, зарплатой, описанием и ссылкой на вакансию.
        """
        return f'{self.profession}\n' \
               f'от {self.payment_from}\n' \
               f'{self.candidat}\n' \
               f'{self.link}\n'

    def __gt__(self, other):
        """
        Операция сравнения "больше" для объектов Vacancy_spj.
        """
        if isinstance(other, Vacancy_spj):
            return self.payment_from > other.payment_from
        raise TypeError('other is not Vacancy object')

    def to_dict(self):
        """
        Возвращает словарь с данными вакансии.
        """
        return {
            "name": self.profession,
            "salary": self.payment_from,
            "description": self.candidat,
            "link": self.link
        }
