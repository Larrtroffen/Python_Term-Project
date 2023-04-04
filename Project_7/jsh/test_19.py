# 创建一个图形类 Shape，包含计算面积和周长的方法。
# 再创建一个三角形类 Triangle，继承自 Shape 类，重写计算面积和周长的方法，实现对三角形的计算
class Shape:
    def __init__(self):
        pass
    def area(self):
        pass
    def perimeter(self):
        pass

class Tritangle(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** (1/2)

    def perimeter(self):
        return self.a + self.b + self.c
