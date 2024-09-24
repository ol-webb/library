class User:

    def __init__(self,name,user_id,books):
        self.name = name
        self._user_id = user_id
        self.books = []


        def withdraw_book(book):
            if book.borrowed == True:
                return(f"cannot withdraw {book.title}, is unavailable")
            
            if book.borrowed == False:
                self.books.append(book)
                book.borrowed = True
                return(f"withdrawn {book.title}")