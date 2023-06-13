from hh.hh_api import HH
from spj.spj_api import SPJ
from hh.utils import get_vacancies, save_vacancies, show_saved_vacancies
from spj.spj_utils import get_vacancies_spj
from json_saver import JSONSaver


def main():
    hh = HH()
    spj = SPJ()
    json_saver = JSONSaver("vacancies.json")
    vacancies = []

    while True:
        print("Выберите одно из действий:")
        print("1. Поиск на HeadHunter по ключевым словам")
        print("2. Поиск на SuperJob по ключевым словам")
        print("3. Сохранить вакансию в JSON")
        print("4. Показать сохраненные вакансии")
        print("5. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            keyword = input("Введите ключевые слова для поиска вакансий: ")
            count = int(input("Введите количество вакансий: "))
            vacancies = get_vacancies(hh, keyword, count)

            if not vacancies:
                print("Нет доступных вакансий.")
            else:
                for i, vacancy in enumerate(vacancies, start=1):
                    print(f"Вакансия #{i}")
                    print(vacancy)

        elif choice == "2":
            keyword = input("Введите ключевые слова для поиска вакансий: ")
            count = int(input("Введите количество вакансий: "))
            vacancies = get_vacancies_spj(spj, keyword, count)

            if not vacancies:
                print("Нет доступных вакансий.")
            else:
                for i, vacancy in enumerate(vacancies, start=1):
                    print(f"Вакансия #{i}")
                    print(vacancy)

        elif choice == "3":
            if not vacancies:
                print("Сначала получите вакансии по ключевым словам.")
            else:
                save_vacancies(json_saver, vacancies)

        elif choice == "4":
            show_saved_vacancies(json_saver)

        elif choice == "5":
            break
        else:
            print("Некорректный ввод. Попробуйте еще раз :)")


if __name__ == '__main__':
    main()
