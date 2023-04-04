class Animal(object):

    def __init__(self,kinds,age,weight):
        super(Animal, self).__init__()
        self.kinds = kinds
        self.age = age
        self.weight = weight

    def print_info(self):
        print(self.kinds + ' ' + self.age + ' ' + self.weight)


class Dog(Animal):
    def __init__(self,age,weight):
        super(Animal, self).__init__()
        self.age = age
        self.weight = weight

    def print_info(self):
        print('Dog'+ ' ' + self.age + ' ' + self.weight)

class Cat(Animal):
    def __init__(self,age,weight):
        super(Animal, self).__init__(age,weight)
        self.age = age
        self.weight = weight

    def print_info(self):
        print('Cat' + ' ' + self.age + ' ' + self.weight)

class Bird(Animal):

    def __init__(self, age, weight, fly):
        super(Animal,self).__init__()
        self.age = age
        self.weight = weight
        self.fly = fly

    def print_info(self):
        print('bird'+' '+self.age+' '+self.weight+' '+self.fly)