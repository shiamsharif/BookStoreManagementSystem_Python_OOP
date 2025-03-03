""" 
1. import book class
2. create file(books.txt)
3. error check
4. add books in the file
"""

# bookstore.py
from book import Book

class BookStore:
    """Handles book-related operations."""

    FILE_NAME = "books.txt"

    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        """Load books from file into memory."""
        books = []
        try:
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    books.append(Book.from_string(line))
        except FileNotFoundError:
            pass  # No books yet
        return books

    def save_books(self):
        """Save all books to file."""
        with open(self.FILE_NAME, "w") as file:
            for book in self.books:
                file.write(book.to_string())
