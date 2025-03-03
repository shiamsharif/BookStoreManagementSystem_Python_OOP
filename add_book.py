""" 
method- 
    1. user add book
    2. price and stock varification not negative
    3. add to the file
"""

# add_book.py
from bookstore import BookStore
from book import Book

def add_book(bookstore):
    """Add a new book to the store, ensuring no duplicate ISBNs exist."""
    print("\n--- Add a New Book ---")
    
    # ✅ Ensure books are loaded first
    bookstore.load_books()  

    isbn = input("Enter ISBN (Unique Book ID): ").strip()

    # ✅ Check if ISBN exists in the loaded books
    for book in bookstore.books:
        if book.isbn == isbn:
            print("❌ A book with this ISBN already exists! Please use a unique ISBN.")
            return

    title = input("Enter Title: ").strip()
    author = input("Enter Author: ").strip()
    genre = input("Enter Genre: ").strip()
    
    try:
        price = float(input("Enter Price: ").strip())
        stock = int(input("Enter Stock Quantity: ").strip())
        if price < 0 or stock < 0:
            print("Price and Stock is not non-negative value.")
            return
    except ValueError:
        print("❌ Invalid price or stock format! Please enter numeric values.")
        return

    new_book = Book(isbn, title, author, genre, price, stock)
    
    # ✅ Append new book & save
    bookstore.books.append(new_book)
    bookstore.save_books()
    print("✅ Book added successfully!")
    








    
    