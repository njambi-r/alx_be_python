# implementing a book class
class Book:
    def __init__(self, title, author):
        title = self.title
        author = self.author
        self._is_checked_out = False
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        return not self._is_checked_out
        
class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out: {title}\n")
                self.list_available_books()
                return
        print(f"Book '{title}' is not available or does not exist.\n")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned: {title}\n")
                self.list_available_books()
                return
        print(f"Book '{title}' is not checked out or does not exist.\n")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"   {book.title} by {book.author}")
        else:
            print("No books available.")
        print("")

    