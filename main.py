from hh.hh_api import HH
from hh.utils import get_vacancies, save_vacancies, show_saved_vacancies
from json_saver import JSONSaver


def main():
    hh = HH()
    json_saver = JSONSaver("vacancies.json")  # Создаем экземпляр JSONSaver
    vacancies = []

    while True:
        print("Выберите одно из действий:")
        print("1. Получить и показать вакансии по ключевым словам")
        print("2. Сохранить вакансию в JSON")
        print("3. Показать сохраненные вакансии")
        print("4. Выход")

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
            if not vacancies:
                print("Сначала получите вакансии по ключевым словам.")
            else:
                save_vacancies(json_saver, vacancies)

        elif choice == "3":
            show_saved_vacancies(json_saver)

        elif choice == "4":
            break

        else:
            print("Некорректный ввод. Попробуйте еще раз.")


if __name__ == '__main__':
    main()
