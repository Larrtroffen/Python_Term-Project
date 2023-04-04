# 为 Email 类的发件人、收件人、主题属性设为私有属性，实现获取、设置私有属性的方法。
class Email:
    def __init__(self, sender, receiver, theme, concept):
        self.__sender = sender
        self.__receiver = receiver
        self.__theme = theme
        self.concept = concept
    def get_sender(self):
        return self.__sender
    def get_receiver(self):
        return self.__receiver
    def get_theme(self):
        return self.__theme
    def get_sender(self, sender):
        self.__sender = sender
    def get_sender(self, receiver):
        self.__receiver = receiver
    def get_sender(self, theme):
        self.__theme = theme