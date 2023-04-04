class Person(object):
    def __init__(self,name,age,gender):
        super(Person, self).__init__()
        self.name = name
        self.__age = age
        self.gender = gender

    def print_info(self):
        print(self.name+' '+self.__age+' '+self.gender)

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age = age