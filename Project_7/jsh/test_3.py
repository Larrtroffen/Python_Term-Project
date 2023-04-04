#继承自 Person 类，新增学校、年级、成绩等属性，以及一个计算平均成绩的方法 average_score。
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def print_info(self):
        print(self.name, self.age, self.gender)

class Student(Person):
    def __init__(self, name, age, gender, school, grade, score1, score2):
        super().__init__(name, age, gender)
        self.__school = school
        self.__grade = grade
        self.__score1 = score1
        self.__score2 = score2
    def average_score(self):
        print((self.__score1+self.__score2)/2.0)

if __name__ == '__main__':
    p = Student('A', 12, 'gril', 'zhenhua', 'grade6', 61, 59)
    p.average_score()
