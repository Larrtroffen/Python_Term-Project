#为 Student 类新增一个类属性 class_name，表示班级名称。
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def print_info(self):
        print(self.name, self.age, self.gender)

class Student(Person):
    def __init__(self, name, age, gender, school, grade, class_name, score1, score2):
        super().__init__(name, age, gender)
        self.school = school
        self.grade = grade
        self.class_name = class_name
        self.score1 = score1
        self.score2 = score2
    def average_score(self):
        print((self.score1+self.score2)/2.0)