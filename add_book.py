""" 
method- user add book
    price and stock varification not negative
"""

from bookstore import BookStore
from book import Book

def add_book(bookstore):
    print("\n--ADD New Bo0k--")
    isbn = input("Enter ISBN or Unique Book ID: ").strip()
   
    if any(book.isbn == isbn for book in bookstore.books):
        print("This ISBN already exists!!!")
        return
    
    title = input("Enter Title: ").strip()
    author = input("Enter Author: ").strip()
    genre = input("Enter Genre: ").strip()
    
    try:
        price = float(input("Enter Price: ").strip())
        stock = int(input("Enter Stock Quantity: ").strip())

        if price < 0 or stock < 0:
            print("Price and stock must be non-negative!")
            return
    except ValueError:
        print("Invalid price or stock format!!")
        return
        
    new_book = Book(isbn, title, author, genre, price, stock)
    bookstore.books.append(new_book)
    bookstore.save_books()
    print("Book added successfully!")
    
    