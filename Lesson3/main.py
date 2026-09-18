from Func import register, login, show_schedule, load_accounts, user_menu


def main():
    load_accounts()
    while True:
        print("\n=================================")
        print("🎬 ДОБРО ПОЖАЛОВАТЬ В КИНОТЕАТР 🎬")
        print("=================================")
        print("1. Зарегистрироваться")
        print("2. Войти")
        print("3. Посмотреть афишу")
        print("0. Выход из программы")

        choice = input("Выберите пункт меню: ").strip()
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                user_menu(user)
        elif choice == "3":
            show_schedule()
        elif choice == "0":
            print("До свидания! Ждём вас в нашем кинотеатре!")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите цифру от 0 до 3.")


if __name__ == "__main__":
    main()