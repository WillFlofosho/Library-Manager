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
            bookDatabase = open(databaseName, 'a')
            bookDatabase.write('\n')
            # get to new line in text file
            bookDatabase.write(book)
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

    # return book and update database, identify if book isn't from this library.
    def returnBook(self, book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print('Book returned successfully. Thank you.')
        else:
            print('The book does not exist in the book lending database.')


# this is the menu. I will be tackling object creation later.
# this menu works as a loop hat runs until the user breaks it.
def main():
    while (True):
        print(f'Welcome ti the {library.name} library. Your options are:')
        choice = '''
        1. Display Books
        2. Checkout a Book
        3. Add a Book
        4. Return a Book
        '''

        print(choice)

        userInput = input('Press Q to quit and C to continue:')
        if userInput == 'C':
            userChoice = int(input('Select an option to continue:'))
            if userChoice == 1:
                library.displayBooks()

            elif userChoice == 2:
                book = input('Enter the name of the book you want to checkout:')
                user = input('Enter the name of the user:')
                library.lendBook(book, user)

            elif userChoice == 3:
                book = input('Enter the name of the book you want to add:')

                library.addBook(book)

            elif userChoice == 4:
                book = input('Enter the name of the book you want to return:')
                library.returnBook(book)

            else:
                print('Please choose a valid option')

        elif userInput =='Q':
            break

        else:
            print('Please enter a valid option')

if __name__ == '__main__':
    booksList = []
    databaseName = input('Enter the name of the database file with extension:')
    bookDatabase = open(databaseName, 'r')
    for book in bookDatabase:
        booksList.append(book)
    library = Library(booksList, 'WilliamF')
    main()