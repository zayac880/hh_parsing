

class Vacancy:
    def __init__(self, name, salary, description, link):
        self.name = name
        self.salary = salary
        self.description = description
        self.link = link

    def __repr__(self):
        return ''

    def __str__(self):
        return f'{self.name}\n' \
               f'{self.salary}\n' \
               f'{self.description}\n' \
               f'{self.link}\n'

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary > other.salary
        raise TypeError('other is not Vacancy object')

    def to_dict(self):
        return {
            'name': self.name,
            'salary': self.salary,
            'description': self.description,
            'link': self.link
        }
