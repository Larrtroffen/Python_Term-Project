class Phone(object):

    def __init__(self,bank,model_num,color,
                 battery):
        super(Phone, self).__init__()
        self.bank = bank
        self.model_num = model_num
        self.color = color
        self.battery = battery

    def phone(self):
        pass

    def send_message(self):
        pass

    def charge(self):
        pass

    phone_brands = [1,2,3]
    @staticmethod
    def get_phone_brands():
        return Phone.phone_brands