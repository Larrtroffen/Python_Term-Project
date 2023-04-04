# 为 Phone 类新增一个静态方法 get_phone_brands，返回所有手机品牌的列表。
class Phone:
    def __init__(self, brand, type, color, rest):
        self.brand = brand
        self.type = type
        self.color = color
        self.rest = rest
    @staticmethod
    def get_phone_brands():
        return ['IPHONE', 'HUAWEI','OPPO', 'VIVO']
    