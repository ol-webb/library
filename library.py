class Library:

    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self,book):
        self.books.append(book)

    def add_user(self,user):
        self.users.append(user)


    def withdraw_book(self,user,book):
        if user not in self.users:
            print('User not in Library')
            return()
        if book not in self.books:
            print("Book not in Library")
            return()

        if book.borrowed == True:
            print(f"cannot withdraw {book.title}, is unavailable")
            return()
        
        if book.borrowed == False:
            user.books.append(book)
            book.borrowed = True
            print(f"withdrawn {book.title}")
            return()

    
    def return_book(self, user, book):

        if user not in self.users:
            print('User not in Library')
            return()
        if book not in self.books:
            print("Book not in Library")
            return()
        

        if book in user.books:
            book.borrowed = False
            user.books.remove(book)
            print(f"'{book.title}' has been returned by {user.name}.")
        else:
            print(f"{user.name} does not have '{book.title}' borrowed.")


    def search_library_book(self,book_title=None,book_author=None,book_ISBN=None):
        if book_title == book_author == book_ISBN == None:
            print("Please provide some book details")
            return

        if book_title != None:
            print('cock')
            for book in self.books:
                if book.title == book_title:
                    print(f"Book in library, available: {book.borrowed}")
            return
        
        elif book_author != None:
            for book in self.books:
                if book.author == book_author:
                    print(f"Matching book by this author: {book.title}. Available: {book.borrowed}")
            return
        
        elif book_ISBN != None:
            for book in self.books:
                if book.ISBN == book_ISBN:
                    print(f"Matching ISBN, available: {book.borrowed}")
            return


            