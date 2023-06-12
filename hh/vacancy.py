class Vacancy:
    """
    Класс, представляющий вакансию.
    name (str): Название вакансии.
    salary (int): Зарплата.
    description (str): Описание вакансии.
    link (str): Ссылка на вакансию.
    """
    def __init__(self, name, salary, description, link):
        """
        Инициализация объекта Vacancy.
        """
        self.name = name
        self.salary = salary
        self.description = description
        self.link = link

    def __str__(self):
        """
        Возвращает строковое представление объекта Vacancy.
        Строка с названием, зарплатой, описанием и ссылкой на вакансию.
        """
        return f'{self.name}\n' \
               f'{self.salary}\n' \
               f'{self.description}\n' \
               f'{self.link}\n'

    def __gt__(self, other):
        """
        Операция сравнения "больше" для объектов Vacancy.
        """
        if isinstance(other, Vacancy):
            return self.salary > other.salary
        raise TypeError('other is not Vacancy object')

    def to_dict(self):
        """
        Возвращает словарь с данными вакансии.
        """
        return {
            "name": self.name,
            "salary": self.salary,
            "description": self.description,
            "link": self.link
        }
