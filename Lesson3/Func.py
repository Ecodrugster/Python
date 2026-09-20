import os
import json
from CinemaAccount import CinemaAccount, StudentCinemaAccount, VIPCinemaAccount

FILE_NAME = "Lesson3/accounts.json"
cinema_accounts = []


MOVIES = [
    {"id": 1, "title": "Интерстеллар", "time": "18:00", "hall": "Зал 1", "price": 450},
    {"id": 2, "title": "Дюна: Часть 2", "time": "20:30", "hall": "IMAX", "price": 600},
    {"id": 3, "title": "Оппенгеймер", "time": "15:00", "hall": "Зал 2", "price": 400},
    {"id": 4, "title": "Человек-паук: Паутина вселенных", "time": "12:00", "hall": "Зал 3", "price": 350},
]


def load_accounts():    
    global cinema_accounts  
    cinema_accounts = []
    if not os.path.exists(FILE_NAME):
        return

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return

    for item in data:
        acc_type = item.get("type", "стандарт")
        if acc_type == "студент":
            user = StudentCinemaAccount(
                item["username"],
                item["password"],
                item.get("balance", 0.0),
                item.get("discount", 0.20)
            )
        elif acc_type == "vip":
            user = VIPCinemaAccount(
                item["username"],
                item["password"],
                item.get("balance", 0.0),
                item.get("cashback_rate", 0.10)
            )
            user.bonus_points = item.get("bonus_points", 0.0)
        else:
            user = CinemaAccount(
                item["username"],
                item["password"],
                item.get("balance", 0.0)
            )
        user.tickets = item.get("tickets", [])
        cinema_accounts.append(user)


def save_accounts():
    data = []
    for account in cinema_accounts:
        if isinstance(account, VIPCinemaAccount):
            acc_type = "vip"
        elif isinstance(account, StudentCinemaAccount):
            acc_type = "студент"
        else:
            acc_type = "стандарт"

        item = {
            "username": account.username,
            "password": account.password,
            "balance": account.balance,
            "type": acc_type,
            "tickets": account.tickets,
        }
        if isinstance(account, StudentCinemaAccount):
            item["discount"] = account.discount
        elif isinstance(account, VIPCinemaAccount):
            item["cashback_rate"] = account.cashback_rate
            item["bonus_points"] = account.bonus_points

        data.append(item)

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def find_account(username):
    for account in cinema_accounts:
        if account.username == username:
            return account
    return None


def validate(password, balance):
    if len(password) < 8:
        print("Пароль должен содержать минимум 8 символа.")
        return False
    if balance < 0:
        print("Начальный баланс не может быть отрицательным.")
        return False
    return True


def register():
    print("\nРегистрация в Кинотеатре")
    username = input("Введите логин: ").strip()
    if not username:
        print("Имя пользователя не может быть пустым.")
        return

    if find_account(username):
        print("Пользователь с таким именем уже существует!")
        return

    password = input("Введите пароль: ").strip()
    try:
        balance = float(input("Введите начальный баланс: "))
    except ValueError:
        print("Ошибка: баланс должен быть числом.")
        return

    if not validate(password, balance):
        return

    print("Типы аккаунтов:")
    print(" 1. Стандарт (обычные цены)")
    print(" 2. Студент (скидка 20% на все билеты)")
    print(" 3. VIP (кэшбэк 10% баллами + бесплатный попкорн)")
    choice = input("Выберите тип аккаунта (1-3): ").strip()

    if choice == "2":
        user = StudentCinemaAccount(username, password, balance)
    elif choice == "3":
        user = VIPCinemaAccount(username, password, balance)
    else:
        user = CinemaAccount(username, password, balance)

    cinema_accounts.append(user)
    save_accounts()
    print(f"Аккаунт '{username}' успешно создан!")


def login():
    print("\n--- Вход в систему ---")
    username = input("Введите логин: ").strip()
    password = input("Введите пароль: ").strip()
    account = find_account(username)

    if account and account.check_password(password):
        print(f"Добро пожаловать в кинотеатр, {username}!")
        return account

    print("Неверный логин или пароль.")
    return None


def show_schedule():
    print("\nАФИША СЕАНСОВ")
    for m in MOVIES:
        print(f"[{m['id']}] '{m['title']}' | {m['hall']} | Время: {m['time']} | Цена: {m['price']}")


def buy_ticket_flow(account):
    show_schedule()
    try:
        movie_id = int(input("Введите номер фильма для покупки: "))
    except ValueError:
        print("Неверный номер фильма.")
        return

    selected_movie = next((m for m in MOVIES if m["id"] == movie_id), None)
    if not selected_movie:
        print("Фильм с таким номером не найден.")
        return

    seat = input("Введите ряд и место (например, 'Ряд 4, Место 7'): ").strip()
    if not seat:
        print("Место не может быть пустым.")
        return

    price_to_pay = account.calculate_ticket_price(selected_movie["price"])
    print(f"Цена для вашего аккаунта: {price_to_pay} (Базовая: {selected_movie['price']})")
    confirm = input("Подтвердить покупку? (да/нет): ").lower().strip()
    if confirm in ("да", "yes"):
        movie_title = f"{selected_movie['title']} ({selected_movie['time']}, {selected_movie['hall']})"
        if account.buy_ticket(movie_title, seat, selected_movie["price"]):
            save_accounts()


def return_ticket_flow(account):
    if not account.tickets:
        print("У вас нет купленных билетов.")
        return

    account.show_tickets()
    try:
        idx = int(input("Введите номер билета для возврата: ")) - 1
        if isinstance(account, VIPCinemaAccount):
            account.return_ticket(idx)
            if account.bonus_points >= 40:
                account.bonus_points -= 40
        else:
            account.return_ticket(idx)
    except ValueError:
        print("Неверный ввод.")
        return

    if account.return_ticket(idx):
        save_accounts()
    


def user_menu(account):
    while True:
        print(f"\n=== Меню зрителя ({account.username}) ===")
        print("1. Посмотреть афишу фильмов")
        print("2. Купить билет")
        print("3. Мои билеты")
        print("4. Сдать билет")
        print("5. Пополнить баланс")
        print("6. Информация об аккаунте")
        print("7. Сменить пароль")
        print("0. Выйти из аккаунта")

        choice = input("Выберите действие: ").strip()
        if choice == "1":
            show_schedule()
        elif choice == "2":
            buy_ticket_flow(account)
        elif choice == "3":
            account.show_tickets()
        elif choice == "4":
            return_ticket_flow(account)
        elif choice == "5":
            try:
                amt = float(input("Введите сумму пополнения: "))
                if account.deposit(amt):
                    save_accounts()
            except ValueError:
                print("Сумма должна быть числом.")
        elif choice == "6":
            account.show_info()
        elif choice == "7":
            new_pwd = input("Введите новый пароль: ").strip()
            if account.password == new_pwd:
                save_accounts()
        elif choice == "0":
            print("Вы вышли из профиля.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")