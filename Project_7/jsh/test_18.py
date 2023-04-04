# 创建一个员工类 Employee，包含姓名、工号、职位、工资等属性，以及打印员工信息
# 的方法 print_info。再创建一个经理类 Manager，继承自 Employee 类，新增部门、下属等属
# 性，重写 print_info 方法，输出经理的信息。
class Employee:
    def __init__(self, name, id, position, salary):
        self.name = name
        self.id = id
        self.position = position
        self.salary = salary

    def print_info(self):
        print(self.name, self.id, self.position, self.salary)


class Manager(Employee):
    def __init__(self, name, id, position, salary, department, subordinates):
        super().__init__(name, id, position, salary)
        self.department = department
        self.subordinates = subordinates

    def print_info(self):
        print(self.name, self.id, self.position, self.salary, self.department, self.subordinates)
