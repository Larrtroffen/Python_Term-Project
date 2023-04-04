# 练习1 练习8
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.__age = age
        self.gender = gender
    def print_info(self):
        print(self.name,self.age,self.gender)
    def get_age(self):
        print(self.__age)
    def set_age(self, age):
        self.__age = age
        
# 练习2
class BankAccount:
    def __init__(self, name, account, balance):
        self.name = name
        self.balance = balance
        self.account = account
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def print_info(self):
        print(self.name,self.balance)
        
# 练习3 练习9 练习17
class Student(Person):
    def __init__(self, name, age, gender, school, grade, class_name, score):
        super().__init__(name, age, gender)
        self.school = school
        self.grade = grade
        self.class_name = class_name
        self.score = score
    def average_score(self):
        return sum(self.score)/len(self.score)
    def print_info(self):
        super.get_age()
        return print(self.name,self.__age,self.gender,self.school,self.grade,self.class_name,self.score)
    
# 练习4 练习10
class Email:
    def __init__(self, sender, receiver, subject, content):
        self.__sender = sender
        self.__receiver = receiver
        self.__subject = subject
        self.content = content
    def get_sender(self):
        return self.__sender
    def get_receiver(self):
        return self.__receiver
    def get_subject(self):
        return self.__subject
    def set_sender(self, sender):
        self.__sender = sender
    def set_receiver(self, receiver):
        self.__receiver = receiver
    def set_subject(self, subject):
        self.__subject = subject    
    def send_email(self):
        print('发件人: {}\n收件人: {}\n主题: {}\n{}'.format(self.__sender, self.__receiver, self.__subject, self.content))
    
# 练习5 练习11 练习12
class Car:
    def __init__(self, brand, model, color, speed):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = speed
    def accelerate(self):
        self.speed += 10
    def brake(self):
        self.speed -= 10
    def print_speed(self):
        print(self.speed)
    def __check_speed(self):
        if self.speed > 200:
            print("最大值")
        elif self.speed < 0:
            print("最小值")
    def get_max_speed(self):
        if self.brand == "奔驰":
            return 250
        elif self.brand == "宝马":
            return 280 
        
# 练习6 练习13
class Phone:
    def __init__(self, brand, model, color, battery):
        self.brand = brand
        self.model = model
        self.color = color
        self.battery = battery
    def call(self):
        print("打电话")
    def send_message(self):
        print("发短信")
    def charge(self):
        self.battery = 100
        print("充电")
    @staticmethod
    def get_phone_brands(self):
        return ["苹果", "华为", "小米", "三星", "OPPO", "VIVO"]
        
# 练习7 练习14
class Book:
    def __init__(self, title, author, press, press_time, book_count):
        self.title = title
        self.author = author
        self.press = press
        self.press_time = press_time
        self.book_count = book_count
    def print_info(self):
        print(self.title,self.author,self.press,self.press_time)
        
# 练习15
class Animal:
    def __init__(self, kind, weight):
        self.kind = kind
        self.weight = weight
    def print_info(self):
        print(self.kind,self.weight)
class Dog(Animal):
    def __init__(self, kind, weight, name):
        super().__init__(kind, weight)
        self.name = name
    def print_info(self):
        print(self.kind,self.weight,self.name)
class Cat(Animal):
    def __init__(self, kind, weight, name):
        super().__init__(kind, weight)
        self.name = name
    def print_info(self):
        print(self.kind,self.weight,self.name)
        
# 练习16
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
    
# 练习17
p = Person("李傲", 19, "男")
Person.print_info(p)

# 练习18
class Employee:
    def __init__(self, name, number, position, salary):
        self.name = name
        self.number = number
        self.position = position
        self.salary = salary
    def print_info(self):
        print(self.name,self.number,self.position,self.salary)    
class Manager(Employee):
    def __init__(self, name, number, position, salary, department, subordinates):
        super().__init__(name, number, position, salary)
        self.department = department
        self.subordinates = subordinates
    def print_info(self):
        print(self.name,self.number,self.position,self.salary,self.department,self.subordinates)
        
# 练习19
class Tritangle(Shape):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
    def perimeter(self):
        return self.a + self.b + self.c
    
# 练习20
class Bird(Animal):
    def __init__(self, kind, weight, fly):
        super().__init__(kind, weight)
        self.fly = fly
    def print_info(self):
        print(self.kind,self.weight,self.fly)
    