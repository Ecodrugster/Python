
# def create_contact_card(**args):
#     for key, value in args.items():
#         print(f"- {key}: {value}")

# create_contact_card(name="Максим",email="ecodrugmaster@gmail.com",city="Алматы")

# def calculate_total(*args,**kwargs):
#     result = 0
#     for i in args:
#         result += i
#     if "discount" in kwargs:
#         for i in args:
#             result -= i * (kwargs["discount"] / 100)
#     return result

# print(calculate_total(140,260,500))
# print(calculate_total(140,260,500,discount=10))

# def logger(func_name, *args, **kwargs):
#     print(f"[LOG] Функция '{func_name}' вызвана")
#     print(f"Аргументы: ", args)
#     print(f"Именнованные аргументы:", kwargs)
    

# logger("send_email",
#         "user@test.com",
#         "Hello!",
#         priority = "high",
#         retry=True)








# class Figure(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass

# class Squre(Figure):
#     def __init__(self, side):
#         self.side = side

#     def get_area(self):
#         return self.side ** 2 

# class Triangle(Figure):
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def get_area(self):
#         return (self.a * self.b) / 2

# class Circle(Figure):
#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         return 3.14 * self.radius ** 2


# figures = [
#     Squre(10),
#     Squre(4),
#     Squre(6),
#     Triangle(10,3),
#     Triangle(3,10),
#     Triangle(5,6),
#     Circle(10)
# ]    


from datetime import datetime
from abc import ABC, abstractmethod


# class Notification(ABC):
#     def __init__(self, msg):
#         self.msg = msg
#     @abstractmethod
#     def send(self,message):
#         pass

# class EmailNotification(Notification):
#     def send(self):
#         print(f"Отправлено по Email: {self.msg}")

# class SMSNotification(Notification):
#     def send(self,message):
#         print(f"Отправлено SMS: {message}")

# notifications = [
#     SMSNotification("asd"),
# ]

# for notification in notifications:
#     notification.send("Привет")
    
from json import dump, load

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

