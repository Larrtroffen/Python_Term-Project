# 创建一个人类 Person，包含姓名、年龄、性别三个属性，以及一个打印个人信息的方法print_info。
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def print_info(self):
        print(self.name, self.age, self.gender)

if __name__ == '__main__':
    p = Person('A', 12, 'gril')
    p.print_info()
