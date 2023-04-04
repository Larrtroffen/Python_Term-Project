class BankAccount(object):
    def __init__(self,name,id,money):
        super(BankAccount, self).__init__()
        self.name = name
        self.id = id
        self.money = money

    def set_money(self,money):
        self.money+=money

    def get_money(self,money):
        self.money-=money

    def see_money(self):
        return self.money
