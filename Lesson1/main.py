
# ЗАДАНИЕ 1

# name = input("Введите ваше имя: ")
# age = int(input("Введите ваш возраст: "))

# print(f"Привет, {name}! Через год тебе будет {age + 1} лет.")



# ЗАДАНИЕ 2

# number = int(input("Введите целое число: "))

# if number > 0:
#     sign = "Положительное"
# elif number < 0:
#     sign = "Отрицательное"
# else:
#     sign = "Ноль"

# if number % 2 == 0:
#     parity = "чётное"
# else:
#     parity = "нечётное"

# print(f"{sign}, {parity}.")


# ЗАДАНИЕ 3

# count = int(input("Сколько товаров вы хотите добавить? "))

# items = []
# total_cost = 0.0

# for i in range(1, count + 1):
#     print(f"\nТовар #{i}:")
#     item_name = input("  Название: ")
#     price = float(input("  Цена: "))
    
#     items.append(item_name)
#     total_cost += price

# print("\nСписок покупок")
# for item in items:
#     print(f"- {item}")

# print(f"\nОбщая стоимость: {total_cost:.2f}")

# ЗАДАНИЕ 4

# student_name = input("Введите имя студента: ")
# grades_str = input("Введите оценки от 1 до 5 через пробел: ")

# grades = [int(g) for g in grades_str.split()]

# if grades:
#     avg_grade = sum(grades) / len(grades)
#     max_grade = max(grades)
#     min_grade = min(grades)

#     print(f"\nСтудент: {student_name}")
#     print(f"Средняя оценка: {avg_grade:.1f}")
#     print(f"Максимальная оценка: {max_grade}")
#     print(f"Минимальная оценка: {min_grade}")

#     if avg_grade >= 4.0:
#         print("Вердикт: Хороший результат")
#     else:
#         print("Вердикт: Нужно повторить тему")
# else:
#     print("Вы не ввели ни одной оценки.")


# ЗАДАНИЕ 5: Todo List с регистрацией

# users = {} 
# todos = {}  


# def register():
#     """Регистрация нового пользователя."""
#     print("\n--- Регистрация ---")
#     username = input("Придумайте логин: ").strip()
    
#     if username in users:
#         print("Ошибка: Пользователь с таким логином уже существует!")
#         return
    
#     password = input("Придумайте пароль: ").strip()
#     users[username] = password
#     todos[username] = []  
#     print(f"Пользователь '{username}' успешно зарегистрирован!")


# def login():
#     """Вход пользователя в систему."""
#     print("\n--- Вход в систему ---")
#     username = input("Введите логин: ").strip()
#     password = input("Введите пароль: ").strip()
    
#     if username in users and users[username] == password:
#         print(f"Добро пожаловать, {username}!")
#         return username
#     else:
#         print("Ошибка: Неверный логин или пароль!")
#         return None


# def add_task(username):
#     """Добавление задачи текущему пользователю."""
#     task = input("\nВведите новую задачу: ").strip()
#     if task:
#         todos[username].append(task)
#         print("Задача успешно добавлена!")
#     else:
#         print("Задача не может быть пустой.")


# def show_tasks(username):
#     """Отображение всех задач текущего пользователя."""
#     user_tasks = todos[username]
#     print(f"\n--- Ваши задачи ({username}) ---")
#     if not user_tasks:
#         print("Список задач пуст.")
#     else:
#         for index, task in enumerate(user_tasks, 1):
#             print(f"{index}. {task}")


# def delete_task(username):
#     """Удаление задачи по её номеру."""
#     user_tasks = todos[username]
#     show_tasks(username)
    
#     if not user_tasks:
#         return
    
#     try:
#         task_num = int(input("\nВведите номер задачи для удаления: "))
#         if 1 <= task_num <= len(user_tasks):
#             removed_task = user_tasks.pop(task_num - 1)
#             print(f"Задача '{removed_task}' успешно удалена!")
#         else:
#             print("Ошибка: Задачи с таким номером не существует.")
#     except ValueError:
#         print("Ошибка: Пожалуйста, введите целое число.")


# def user_menu(username):
#     """Главное меню личного кабинета пользователя."""
#     while True:
#         print(f"\n=== МЕНЮ ПОЛЬЗОВАТЕЛЯ ({username}) ===")
#         print("1 — Добавить задачу")
#         print("2 — Показать задачи")
#         print("3 — Удалить задачу")
#         print("0 — Выйти из аккаунта")
        
#         choice = input("Выберите действие: ").strip()
        
#         match choice:
#             case "1":
#                 add_task(username)
#             case "2":
#                 show_tasks(username)
#             case "3":
#                 delete_task(username)
#             case "0":
#                 print(f"Вы вышли из аккаунта {username}.")
#                 break
#             case _:
#                 print("Неверный выбор. Попробуйте снова.")


# def main():
#     """Запуск основного цикла программы."""
#     while True:
#         print("\n=== ГЛАВНОЕ МЕНЮ ===")
#         print("1 — Зарегистрироваться")
#         print("2 — Войти")
#         print("0 — Выйти из программы")
        
#         choice = input("Выберите действие: ").strip()
        
#         match choice:
#             case "1":
#                 register()
#             case "2":
#                 current_user = login()
#                 if current_user:
#                     user_menu(current_user)
#             case "0":
#                 print("До свидания!")
#                 break
#             case _:
#                 print("Неверный выбор. Попробуйте снова.")


# main()