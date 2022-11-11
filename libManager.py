# Library class with library name, booklist, and booklender dictionary
class Library:

    def init(self, booksList, name):
        self.booksList = booksList
        self.name = name
        self.lendDict = {}

    # displays books available to checkout
    def displayBooks(self):
        print(f'We have following books in our library:{self.name}')
        for book in self.booksList:
            print(book)

    # Adds book to database if not already present
    def addBook(self, book):
        if book in booksList:
            print('Book already exists')
        else:
            self.booksList.append(book)
            print('Book added')

    # Checkout book and update database, provide name of who checked out a book, and apologize for not having a book
    # in the library
    def lendBook(self, book, user):
        if book in booksList:
            if book not in self.lendDict.keys():
                self.lendDict.update({book: user})
                print('Book has been checked out. Database updated.')
            else:
                print(f'Book has been checked out by {self.lendDict[book]}')
        else:
            print("I'm sorry, we don't have this book in our library.")

    #return book and update database, identify if book isn't from this library.
    def returnBook(self, book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print('Book returned successfully. Thank you.')
        else:
            print('The book does not exist in the book lending database.')
