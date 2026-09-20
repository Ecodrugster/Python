class CinemaAccount:
    def __init__(self, username, password, balance=0.0):
        self.username = username
        self._password = password
        self.balance = float(balance)
        self.tickets = []

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        if new_password:
            self._password = new_password
            print("Пароль успешно изменён.")
            return True
        print("Пароль не может быть пустым.")
        return False

    def check_password(self, password):
        return self._password == password

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Баланс пополнен на {amount} Текущий баланс: {self.balance}")
            return True
        print("Сумма пополнения должна быть положительной.")
        return False

    def calculate_ticket_price(self, base_price):
        return base_price

    def buy_ticket(self, movie, seat, base_price):
        final_price = self.calculate_ticket_price(base_price)
        if self.balance >= final_price:
            self.balance -= final_price
            ticket = {
                "movie": movie,
                "seat": seat,
                "price": final_price
            }
            self.tickets.append(ticket)
            print(f"Билет на '{movie}' (место: {seat}) успешно куплен за {final_price}. Остаток: {self.balance}")
            return True
        else:
            print(f"Недостаточно средств. Стоимость: {final_price}, ваш баланс: {self.balance}")
            return False

    def return_ticket(self, index):
        if 0 <= index < len(self.tickets):
            refund_ticket = self.tickets.pop(index)
            refund_amount = refund_ticket["price"]
            self.balance += refund_amount
            print(f"Билет на '{refund_ticket['movie']}' возвращен. Возврат: {refund_amount} Баланс: {self.balance}")
            return True
        else:
            print("Билет с таким номером не найден.")
            return False

    def show_info(self):
        print(f"\n Аккаунт: {self.username} (Стандартный)")
        print(f"Баланс: {self.balance}")
        print(f"Куплено билетов: {len(self.tickets)}")
        self.show_tickets()

    def show_tickets(self):
        if not self.tickets:
            print("Список билетов пуст.")
            return
        print("Ваши билеты:")
        for idx, t in enumerate(self.tickets, start=1):
            print(f"  {idx}. Фильм: '{t['movie']}' | Место: {t['seat']} | Цена: {t['price']}")


class StudentCinemaAccount(CinemaAccount):
    def __init__(self, username, password, balance=0.0, discount=0.20):
        super().__init__(username, password, balance)
        self.discount = float(discount)

    def calculate_ticket_price(self, base_price):
        discount_amount = base_price * self.discount
        return round(base_price - discount_amount, 2)

    def show_info(self):
        print(f"\n Аккаунт: {self.username} (Студенческий)")
        print(f"Баланс: {self.balance}")
        print(f"Скидка на билеты: {int(self.discount * 100)}%")
        print(f"Куплено билетов: {len(self.tickets)}")
        self.show_tickets()


class VIPCinemaAccount(CinemaAccount):
    "VIP аккаунт: кэшбэк бонусами 10% и бесплатный попкорн при каждой покупке"
    def __init__(self, username, password, balance=0.0, cashback_rate=0.10):
        super().__init__(username, password, balance)
        self.cashback_rate = float(cashback_rate)
        self.bonus_points = 0.0

    def buy_ticket(self, movie, seat, base_price):
        success = super().buy_ticket(movie, seat, base_price)
        if success:
            cashback = round(base_price * self.cashback_rate, 2)
            self.bonus_points += cashback
            print(f"VIP-бонус: Начислено {cashback} бонусов (всего: {self.bonus_points}).")
            print("Вам положен бесплатный VIP-попкорн и напиток в баре!")
        return success

    def show_info(self):
        print(f"\n Аккаунт: {self.username} (VIP)")
        print(f"Баланс: {self.balance}")
        print(f"Бонусные баллы: {self.bonus_points}")
        print(f"Ставка кэшбэка: {int(self.cashback_rate * 100)}%")
        print(f"Куплено билетов: {len(self.tickets)}")
        self.show_tickets()