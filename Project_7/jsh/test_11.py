# 为 Car 类新增一个私有方法_check_speed，在加速和减速时调用该方法判断速度是否超
# 过最大值或最小值。
class Car:
    def __init__(self, brand, type, color, speed, minspeed, maxspeed):
        self.brand = brand
        self.type = type
        self.color = color
        self.speed = speed
        self.minspeed = minspeed
        self.maxspeed = maxspeed
    def capture(self):
        print(self.speed)
    def __check_speed(self):
        if self.speed < self.minspeed or self.speed >self.maxspeed:
            return False