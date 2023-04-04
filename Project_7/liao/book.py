class Book(object):

    book_count = 100
    def __init__(self, name, author, publisher,
                 date):
        super(Book, self).__init__()
        self.name = name
        self.author = author
        self.pulisher = publisher
        self.date = date

    def print_info(self):
        print(self.name+' '+self.author+' '+self.pulisher+' '+self.date)

