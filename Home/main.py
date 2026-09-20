import json


# ЗАДАНИЕ 1

# prices = [1200, 3500, 800, 2100, 5000, 1700]

# print("1. Первые три цены:", prices[:3])

# print("2. Последние две цены:", prices[-2:])

# print("3. В обратном порядке:", prices[::-1])

# print(f"4. Мин: {min(prices)}, Макс: {max(prices)}, Количество: {len(prices)}")
# print()


# ЗАДАНИЕ 2

# students = [
#     {"name": "Анна", "grade": 5},
#     {"name": "Иван", "grade": 4},
#     {"name": "Олег", "grade": 3}
# ]

# students.append({"name": "Мария", "grade": 5})

# for student in students:
#     if student["name"] == "Иван":
#         student["grade"] = 5

# print("Каталог студентов:")
# for student in students:
#     print(f"- Студент: {student['name']}, Оценка: {student['grade']}")
# print()

#  ЗАДАНИЕ 3

# user_note = input("Введите текст заметки: ")

# with open("Home/notes.txt", "a", encoding="utf-8") as file:
#     file.write(user_note + "\n")

# print("\nСодержимое файла notes.txt:")
# with open("Home/notes.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)



#  ЗАДАНИЕ 4

# books = [
#     {"title": "Гарри Поттер", "year": 1997},
#     {"title": "Маленький принц", "year": 1943}
# ]

# with open("Home/books.json", "w", encoding="utf-8") as file:
#     json.dump(books, file, ensure_ascii=False, indent=4)
# print("Данные успешно сохранены в books.json")

# with open("Home/books.json", "r", encoding="utf-8") as file:
#     loaded_books = json.load(file)

# print("\nКниги из JSON-файла:")
# for book in loaded_books:
#     print(f"- Книга: «{book['title']}», Год: {book['year']}")
# print()



#  ЗАДАНИЕ 5

class Film:
    def __init__(self, title, rating):
        self.title = title
        self.__rating = None
        self.set_rating(rating)  

    def show_info(self):
        print(f"Фильм: «{self.title}», Рейтинг: {self.__rating}")

    def get_rating(self):
        return self.__rating

    def set_rating(self, new_rating):
        if 0 <= new_rating <= 10:
            self.__rating = new_rating
        else:
            print(f"Ошибка: Рейтинг {new_rating} выходить за пределы от 0 до 10!")


movie = Film("Интерстеллар", 8.6)


movie.show_info()

print("Текущий рейтинг через get_rating():", movie.get_rating())


movie.set_rating(9.2)
print("Новый рейтинг через get_rating():", movie.get_rating())

movie.set_rating(15) 
movie.show_info()