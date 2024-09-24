class Book:

    def __init__(self,title,author,ISBN,borrowed):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.borrowed = borrowed

    def is_borrowed(self):
        return self.borrowed
    
    