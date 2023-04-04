class Employee(object):
    def __init__(self, name, number, position, salary):
        self.name = name
        self.number = number
        self.position = position
        self.salary = salary
    def print_info(self):
        print(self.name+' '+self.number+' '+self.position+' '+self.salary)

class Manager(Employee):
    def __init__(self, name, number, position, salary, department, subordinates):
        super(Employee,self).__init__(name, number, position, salary)
        self.department = department
        self.subordinates = subordinates

    def print_info(self):
        print(self.name+' '+self.number+' '+self.position+' '+self.salary+' '+self.department+' '+self.subordinates)

