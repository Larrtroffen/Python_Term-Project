# 创建一个汽车类 Car，包含品牌、型号、颜色、速度等属性，以及加速、减速、获取当
# 前速度等方法。
class Car:
    def __init__(self, brand, type, color, speed):
        self.brand = brand
        self.type = type
        self.color = color
        self.speed = speed
    def capture(self):
        print(self.speed)

if __name__ == '__main__':
    c = Car('Ferrari', '488 GTB', 'Rosso Corsa', '330公里')
    c.capture()