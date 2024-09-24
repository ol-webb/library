from book import Book
from user import User
from library import Library

library=Library()

book_data = """
Mr Nice,Jez,123456
The Idiot,Dostoevsky,234567
Crime and Punishment,Dostoevsky,345678
Brothers Karamazov,Dostoevsky,456789
Pride and Prejudice,Jane Austen,567890
Emma,Jane Austen,678901
1984,George Orwell,789012
Animal Farm,George Orwell,890123
Moby Dick,Herman Melville,901234
War and Peace,Leo Tolstoy,123987
"""

book_list = book_data.strip().split('\n')
for book in book_list:
    title, author, isbn = book.split(',')
    new_book = Book(title, author, isbn, True)
    library.add_book(new_book)


mark = User('Mark','8493',None)

library.add_user(mark)

print('running')
library.search_library_book(book_author='Dostoevsky')
print('ran')