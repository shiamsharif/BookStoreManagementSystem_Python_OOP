""" 
1. import book class
2. create file(books.txt)
3. error check
4. add books in the file
"""

# bookstore.py
from book import Book

class BookStore:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.books = [] 

    def load_books(self):
        """Load books from file into memory."""
        self.books = []  
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    isbn, title, author, genre, price, stock = line.strip().split("|")
                    self.books.append(Book(isbn, title, author, genre, float(price), int(stock)))
        except FileNotFoundError:
            print("⚠️ No book data found. Starting fresh.")

    def save_books(self):
        """Save books to file."""
        with open(self.filename, "w") as file:
            for book in self.books:
                file.write(f"{book.isbn} | {book.title} | {book.author} | {book.genre} | {book.price}  |  {book.stock}\n")

