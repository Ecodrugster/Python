from json import dump, load
from datetime import datetime
from abc import ABC, abstractmethod

# Задание 1

# class PaymentMethod(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass

# class CreditCard(PaymentMethod):
#     def __init__(self,balance):
#         self.balance = balance

#     def pay(self,amount):
#         if self.balance < amount:
#             print(f"Недостаточно средств")
#         else:
#             self.balance -= amount
#             print(f"Списано {amount} с карты. Остаток {self.balance}")

# class Paypal(PaymentMethod):
#     def pay(self,amount):
#         print(f"Перевод {amount} через Paypal успешно выполнен")

# def process_order(payment_method,amount):
#     if isinstance(payment_method,PaymentMethod):
#         try:
#             payment_method.pay(amount)
#             return {
#             "method" : payment_method.__class__.__name__,
#             "amount" : amount,
#             "balance" : payment_method.balance,
#             "time" : str(datetime.now().time())
#             }
#         except Exception as e:
#             print(f"Ошибка: {e}")
#             return {}
    
# def load_history(filename):
#     with open(filename,"r") as file:
#         return load(file)

# history_json = load_history("history.json")

# def save_history(history_json,filename):
#     with open(filename,"w") as file:
#         dump(history_json,file,ensure_ascii=False, indent=4)

# Cards = [
#     Paypal()
# ]

# for card in Cards:
#     history_json.append(process_order(card,100))

# save_history(history_json,"history.json")


# Задание 2

class Hero(ABC):
    @abstractmethod
    def attack():
        pass

class Warrior(Hero):
    def __init__(self,name,damage):
        self.name = name
        self.damage = damage

    def attack(self):
        print(f"{self.name} атакует мечом на {self.damage} урона!")

class Mage(Hero):
    def __init__(self,name,damage):
        self.name = name
        self.damage = damage

    def attack(self):
        print(f"{self.name} атакует магией на {self.damage} урона!")


heroes = [
    Warrior("Сильвестр", 50),
    Mage("Ирэн", 70)
]

for hero in heroes:
    if isinstance(hero,Hero):
        hero.attack()
    else:
        print(f"Ошибка: {hero} не является героем")

