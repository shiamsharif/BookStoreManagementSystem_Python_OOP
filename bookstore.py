""" 
1. import book class
2. create file(books.txt)
3. error check
4. add books in the file
"""

from book import Book

class BookStore:
    FILE_NAME = "books.txt"

    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        """load books file to memory."""
        books = []
        try:
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    books.append(Book.from_string(line))
        except FileNotFoundError:
            pass  # No books yet
        return books

    def save_books(self):
        """save all books is file"""
        with open(self.FILE_NAME, "w") as file:
            for book in self.books:
                file.write(book.to_string())

