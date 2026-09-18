from bank_account import BankAccount, PremiumAccount, SavingsAccount
from json import dump, load

FILE_NAME = "C:/Users/Singularity/Desktop/Python/Lesson 2/bankaccount/accounts.json"
bank_accounts = []


def load_accounts():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = load(file)
    except FileNotFoundError:
        return

    for item in data:
        account_type = item.get("type", "стандарт")
        if account_type == "премиум":
            user = PremiumAccount(item["username"], item["password"], item["balance"], item.get("bonus_rate", 0.01))
            user.bonus += item["balance"] * 0.01
        elif account_type == "накопительный":
            user = SavingsAccount(item["username"], item["password"], item["balance"], item.get("interest_rate", 0.15))
            user.interest += item["balance"] * 0.15
        else:
            user = BankAccount(item["username"], item["password"], item["balance"])

        bank_accounts.append(user)

    save_accounts()


def save_accounts():
    data = []
    for account in bank_accounts:
        data.append({
            "username": account.username,
            "password": account.password,
            "balance": account.balance,
            "type": "премиум" if isinstance(account, PremiumAccount) else "накопительный" if isinstance(account, SavingsAccount) else "стандарт",
            "bonus_rate": account.bonus_rate if isinstance(account, PremiumAccount) else None,
            "bonus": account.bonus if isinstance(account, PremiumAccount) else None,
            "interest_rate": account.interest_rate if isinstance(account, SavingsAccount) else None,
            "interest": account.interest if isinstance(account, SavingsAccount) else None
        })
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        dump(data, file, ensure_ascii=False, indent=4)


def find_account(username):
    for account in bank_accounts:
        if account.username == username:
            return account
    return None


def register(username, password, balance, account_type):
    if find_account(username):
        print("Аккаунт уже существует")
        return False
    if not validate(password, balance):
        return False

    account_type_clean = account_type.lower().strip()
    if "премиум" in account_type_clean:
        user = PremiumAccount(username, password, balance, 0.01)
    elif "накопительный" in account_type_clean:
        user = SavingsAccount(username, password, balance, 0.15)
    else:
        user = BankAccount(username, password, balance)
    bank_accounts.append(user)
    save_accounts()
    return True

def validate(password, balance):
    if len(password) < 8:
        print("Пароль должен быть не менее 8 символов")
        return False
    if balance < 0:
        print("Баланс должен быть положительным")
        return False
    return True

def login(username, password):
    for account in bank_accounts:
        if account.username == username and account.password == password:
            print("Вы успешно вошли в аккаунт")
            return account
    print("Неверный логин или пароль")
    return None


def read_amount(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Нужно ввести число")
        return None


def main(account):
    while True:
        print("\n1. Пополнение баланса")
        print("2. Снятие")
        print("3. Просмотр баланса")
        print("4. Перевод")
        print("5. Сменить пароль")
        print("6. Сменить имя")
        print("0. Выйти")
        choice = input("Выберите действие: ")

        match choice:
            case "1":
                amount = read_amount("Введите сумму: ")
                if amount is not None:
                    account.deposit(amount)
                    save_accounts()
            case "2":
                amount = read_amount("Введите сумму: ")
                if amount is not None:
                    account.withdraw(amount)
                    save_accounts()
            case "3":
                account.show_info()
            case "4":
                amount = read_amount("Введите сумму: ")
                if amount is None:
                    continue
                other_name = input("Введите имя пользователя: ")
                other_account = find_account(other_name)
                if other_account is None:
                    print("Аккаунт не найден")
                elif other_account is account:
                    print("Нельзя перевести самому себе")
                else:
                    account.transfer(amount, other_account)
                    save_accounts()
            case "5":
                new_password = input("Введите новый пароль: ")
                account.set_password(new_password)
                save_accounts()
            case "6":
                new_username = input("Введите новое имя пользователя: ")
                if new_username != account.username and find_account(new_username):
                    print("Аккаунт уже существует")
                else:
                    account.set_username(new_username)
                    save_accounts()
            case "0":
                print("Вы вышли из аккаунта")
                break
            case _:
                print("Неверный выбор")


load_accounts()
while True:
    print("\n1. Зарегистрироваться")
    print("2. Войти")
    print("0. Выйти")
    choice = input("Выберите действие: ")
    match choice:
        case "1":
            account_type = input("Введите тип аккаунта - стандарт, премиум, накопительный: ")
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            balance = read_amount("Введите баланс: ")
            if balance is not None:
                register(username, password, balance, account_type)
        case "2":
            username = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            account = login(username, password)
            if account:
                main(account)
        case "0":
            print("Пока!")
            break
        case _:
            print("Неверный выбор")
