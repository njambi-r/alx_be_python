# Base class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"Book: {self.title}, Author: {self.author}"

# Derived classes EBook and PrintBook
class EBook(Book):
    def __init__(self, title, author, file_size:int):
        super().__init__(title, author)
        self.file_size = file_size
        
    def __str__(self):
        return f"EBook: {self.title}, Author: {self.author}, File Size: {self.file_size}MB"

class PrintBook(Book):
    def __init__(self, title, author, page_count:int):
        super().__init__(title, author)
        self.page_count = page_count
        
    def __str__(self):
        return f"PrintBook: {self.title}, Author: {self.author}, Page Count: {self.page_count}"

# Composition - Library
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def list_books(self):
        for book in self.books:
            print(str(book))


