from src.hh_api import HH
from src.vacancy import Vacancy
from src.json_saver import JSONSaver


def main():
    hh = HH()
    vacancies = []

    while True:
        print("Выберите одно из действий:")
        print("1. Получить вакансии по ключевым словам")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Получить вакансии в отсортированном виде")
        print("4. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            keyword = input("Введите ключевые слова для поиска вакансий: ")
            count = int(input("Введите количество вакансий: "))
            vacancies = hh.get_request(keyword, count)
            vacancies = [
                Vacancy(
                    name=item['name'],
                    salary=item['salary']['to'] if item['salary'] else None,
                    description=item['snippet']['responsibility'],
                    link=item['alternate_url']
                ) for item in vacancies
            ]
            for item in vacancies:
                print(item)

        elif choice == "2":
            count = int(input("Введите количество вакансий: "))
            sorted_vacancies = sorted(vacancies, key=lambda x: x.salary if x.salary is not None else float('-inf'), reverse=True)
            top_n_vacancies = sorted_vacancies[:count]
            for item in top_n_vacancies:
                print(item)

        elif choice == "3":
            sorted_vacancies = sorted(vacancies, key=lambda x: x.name)
            for item in sorted_vacancies:
                print(item)

        elif choice == "4":
            break

        else:
            print("Некорректный ввод. Попробуйте еще раз.")


if __name__ == '__main__':
    main()
