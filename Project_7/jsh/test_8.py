# 为 Person 类的年龄属性设为私有属性，实现获取、设置私有属性的方法。
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.__age = age
        self.gender = gender
    def getage(self):
        return self.__age