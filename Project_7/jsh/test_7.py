# 创建一个图书类 Book，包含书名、作者、出版社、出版日期等属性，以及打印书籍信息
# 的方法 print_info。
class Book:
    def __init__(self, name, author, press, date):
        self.name = name
        self.author = author
        self.press = press
        self.date = date
    def print_info(self):
        print(self.name, self.author, self.press, self.date)

if __name__ == '__main__':
    b = Book('hello', 'J', 'QS', '2023-4-3')
    b.print_info()