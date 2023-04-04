# 创建一个动物类 Animal，包含种类、年龄、体重等属性，以及一个打印动物信息的方法 print_info。
# 再创建一个鸟类 Bird，继承自 Animal 类，新增飞行距离等属性，重写 print_info方法，输出鸟的信息。
class Animal:
    def __init__(self, kind, weight):
        self.kind = kind
        self.weight = weight
    def print_info(self):
        print(self.kind, self.weight)

class Bird(Animal):
    def __init__(self, kind, weight, distance):
        super().__init__(kind, weight)
        self.distance = distance
    def print_info(self):
        print(self.kind, self.weight, self.distance)