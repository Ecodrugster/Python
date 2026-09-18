class BankAccount:
    def __init__(self, username, password, balance):
        self.username = username
        self._password = password
        self.balance = balance
        print(f"Аккаунт {self.username} создан, баланс: {self.balance}")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        if new_password:
            self._password = new_password
            print("Пароль изменен")
            return True
        else:
            print("Пароль не может быть пустым")
            return False

    def check_password(self, password):
        if self._password == password:
            print("Пароль верный")
            return True
        else:
            print("Пароль неверный")
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Баланс пополнен на {amount}, текущий баланс: {self.balance}")
            return True
        else:
            print("Сумма пополнения должна быть положительной")
            return False

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Сумма {amount} снята, текущий баланс: {self.balance}")
                return True
            else:
                print("Недостаточно средств")
                return False
        else:
            print("Сумма снятия должна быть положительной")
            return False

    def show_info(self):
        print(f"Имя пользователя: {self.username}")
        print(f"Баланс: {self.balance}")

    def transfer(self, amount, other_account):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                other_account.balance += amount
                print(f"Сумма {amount} переведена на аккаунт {other_account.username}")
                return True
            else:
                print("Недостаточно средств")
                return False
        else:
            print("Сумма перевода должна быть положительной")
            return False

    def get_balance(self):
        return self.balance

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def set_balance(self, balance):
        if balance > 0:
            self.balance = balance
            print(f"Баланс изменен на {balance}, текущий баланс: {self.balance}")
            return True
        else:
            print("Баланс должен быть положительным")
            return False

    def set_username(self, username):
        if username:
            self.username = username
            print(f"Имя пользователя изменено")
            return True
        else:
            print("Имя пользователя не может быть пустым")
            return False

    def set_password(self, password):
        if password:
            self.password = password
            print(f"Пароль изменен")
            return True
        else:
            print("Пароль не может быть пустым")
            return False


class PremiumAccount(BankAccount):
    def __init__(self, username, password, balance, bonus_rate):
        super().__init__(username, password, balance)
        self.bonus_rate = bonus_rate
        self.bonus = 0

    def show_info(self):
        super().show_info()
        print(f"\tБонусная ставка: {self.bonus_rate}")
        print(f"\tБонус: {self.bonus}")

    def withdraw(self, amount):
        if super().withdraw(amount):
            self.bonus += amount * self.bonus_rate


class SavingsAccount(BankAccount):
    def __init__(self, username, password, balance, interest_rate):
        super().__init__(username, password, balance)
        self.interest_rate = interest_rate
        self.interest = 0

    def show_info(self):
        super().show_info()
        print(f"\tПроцентная ставка: {self.interest_rate}")
        print(f"\tДепозит: {self.interest}")


    def withdraw(self, amount):
        if super().withdraw(amount):
            self.interest += amount * self.interest_rate

