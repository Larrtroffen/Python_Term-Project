class Email(object):
    def __init__(self,send_name,get_name,topic,message):
        super(Email, self).__init__()
        self.__send_name = send_name
        self.__get_name = get_name
        self.__topic = topic
        self.message = message

    def send_email(self):
        pass

    def get_send_name(self):
        return self.__send_name

    def set_send_name(self,name):
        self.__send_name = name

    def get_get_name(self):
        return self.__get_name

    def set_get_name(self,name):
        self.__get_name = name

    def get_topic(self):
        return self.__topic

    def set_topic(self,topic):
        self.__topic = topic

