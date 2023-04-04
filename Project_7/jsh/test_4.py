# 创建一个邮件类 Email，包含发件人、收件人、主题、内容等属性，以及发送邮件的方法
# send_email。
class Email:
    def __init__(self, sender, receiver, theme, concept):
        self.sender = sender
        self.receive = receiver
        self.theme = theme
        self.concept = concept
    def send_email(self):
        pass
