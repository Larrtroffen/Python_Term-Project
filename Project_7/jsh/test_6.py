# 创建一个手机类 Phone，包含品牌、型号、颜色、剩余电量等属性，以及打电话、发短
# 信、充电等方法。
class Phone:
    def __init__(self, brand, type, color, rest):
        self.brand = brand
        self.type = type
        self.color = color
        self.rest = rest

    def call(self):
        pass
    def message(self):
        pass
    def charge(self):
        pass