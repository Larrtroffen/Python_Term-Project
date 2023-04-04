# 为 Book 类新增一个类属性 book_count，表示已经出版的书籍数量。
class Book:
    def __init__(self, name, author, press, date, book_count):
        self.name = name
        self.author = author
        self.press = press
        self.date = date
        self.book_count = book_count
