class Car(object):
    max_speed = 120
    min_speed = 60
    def __init__(self,bank,model_number,color,speed):
        super(Car, self).__init__()
        self.bank = bank
        self.model_number = model_number
        self.color = color
        self.speed = speed

    def add_speed(self,speed):
        self.speed+=speed
        self._check_speed()

    def reduce_speed(self,speed):
        self.speed-=speed
        self._check_speed()

    def get_speed(self):
        return self.speed

    def _check_speed(self):
        if self.speed > 120:
            print("超速了")
        elif self.speed < 60:
            print("小于最小速度了")

    @classmethod
    def get_max_speed(cls):
        return Car.max_speed

