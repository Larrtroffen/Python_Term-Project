#为 Car 类新增一个类方法 get_max_speed，返回该汽车品牌的最大速度。
class Car:
    def __init__(self, brand, type, color, speed):
        self.brand = brand
        self.type = type
        self.color = color
        self.speed = speed
    def get_max_speed(self):
        if self.brand == 'a':
            return 888
