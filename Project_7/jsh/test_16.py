# 创建一个形状类 Shape，包含计算面积和周长的方法。再创建两个子类 Rectangle 和
# Circle，分别重写计算面积和周长的方法，实现对矩形和圆形的计算
class Shape:
    def __init__(self):
        pass
    def area(self):
        pass
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius