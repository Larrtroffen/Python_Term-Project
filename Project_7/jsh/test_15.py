# 创建一个动物类 Animal，包含种类、年龄、体重等属性，以及一个打印动物信息的方
# 法 print_info。再创建两个子类 Dog 和 Cat，分别重写 print_info 方法，输出狗和猫的信息。
class Animal:
    def __init__(self, kind, weight):
        self.kind = kind
        self.weight = weight
    def print_info(self):
        print(self.kind, self.weight)
# 子类1
class Dog(Animal):
    def __init__(self, kind, weight, name):
        super().__init__(kind, weight)
        self.name = name
    def print_info(self):
        print(self.kind, self.weight, self.name)
# 子类2
class Cat(Animal):
    def __init__(self, kind, weight, name):
        super().__init__(kind, weight)
        self.name = name
    def print_info(self):
        print(self.kind, self.weight, self.name)