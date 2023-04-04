# 创建一个人类 Person，包含姓名、年龄、性别三个属性，以及一个打印个人信息的方法
# print_info。再创建一个学生类 Student，继承自 Person 类，新增学校、年级、成绩等属性，
# 以及一个计算平均成绩的方法 average_score，重写 print_info 方法，输出学生的信息。
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
        self.school = school
        self.grade = grade
        self.score1 = score1
        self.score2 = score2
    def average_score(self):
        print((self.score1+self.score2)/2.0)
    def print_info(self):
        return self.name, self.age, self.gender, self.school, self.grade, self.score1, self.score2

if __name__ == '__main__':
    p = Student('A', 12, 'gril', 'zhenhua', 'grade6', 61, 59)
    print(p.print_info())
