# 创建一个银行账户类 BankAccount，包含账户名、账号、余额等属性，以及存款、取款、
# 查询余额等方法
class BankAccount:
    def __init__(self, name, id, rest):
        self.name = name
        self.id = id
        self.rest = rest
    def deposit(self, m1):
        self.rest += m1
        print(self.rest)
    def withdrawal(self, m2):
        self.rest -= m2
        print(self.rest)
    def check(self):
        print(self.rest)

if __name__ == '__main__':
    b = BankAccount('biu', 888, 6666)
    b.check()