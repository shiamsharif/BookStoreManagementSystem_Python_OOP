""" 
book- id,title,author,genre,price,stock
    1. __str__ method
    2. to string method
    3. from string method
"""

class Book:
    def __init__(self, isbn, title, author, genre, price, stock):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.stock = stock
        
    def __str__(self):
        return f"Book: {self.title} by {self.author} ({self.genre}) - ${self.price}, Stock: {self.stock}"


    def to_string(self):
        return f"{self.isbn} | {self.title} | {self.author} | {self.genre} | {self.price} | {self.stock}\n"

    @staticmethod
    def from_string(book_string):
        isbn, title, author, genre, price, stock = book_string.strip().split("|")
        return Book(isbn, title, author, genre, float(price), int(stock))


