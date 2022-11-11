# Library class with library name, booklist, and booklender dictionary
class Library:
    def init(self, booksList, name):
        self.booksList = booksList
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f'We have following books in our library:{self.name}')
        for book in self.booksList:
            print(book)

    def addBook(self, book):
        if book in booksList:
            print('Book already exists')
        else:
            self.booksList.append(book)
            print('Book added')

    def lendBook(self, book, user):
        if book in booksList:
            if book not in self.lendDict.keys():
                self.lendDict.update({book: user})
                print('Book has been checked out. Database updated.')
            else:
                print(f'Book has been checked out by {self.lendDict[book]}')
        else:
            print("I'm sorry, we don't have this book in our library.")

    