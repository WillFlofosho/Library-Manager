

# Library class with library name, booklist, and booklender dictionary
class Library:
    def init (self, bookslist, name):
        self.booksList = bookslist
        self.name = name
        self.lendDict = {}
