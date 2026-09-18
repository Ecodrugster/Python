import json

# student = {
#     "name": "Иван",
#     "grade": "3"
# }

# with open("test.json", "w", encoding="utf-8") as file:
#     json.dump(student, file, ensure_ascii=False, indent=4)

# with open("test.json", "r", encoding="utf-8") as file:
#     new_student = json.load(file)
# print(new_student)
# print(new_student["name"])
# print(type(new_student))

# text = json.dumps(student, ensure_ascii=False, indent=4)
# print(text)
# print(type(text))

# dict = json.loads(text)
# print(dict)
# print(type(dict))

# test = {
#     "name": 123
# }
# test["city"] = "Москва"

# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
        
#     @property
#     def grade(self):
#         return self._grade

#     @grade.setter
#     def grade(self, new_grade):
#         self._grade = new_grade

#     def show_info(self):
#         print(f"{self.name} {self.grade}")

# student = Student("Иван", "3")
# student.show_info()
# print(student.grade)
# student.grade = 5

