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
    print("\n--- Add a New Book ---")
    
    isbn = input("Enter ISBN (Unique Book ID): ").strip()
    
    # Check if ISBN already exists
    if any(book.isbn == isbn for book in bookstore.books):
        print("❌ This ISBN already exists!")
        return

    title = input("Enter Title: ").strip()
    if not title or title.istitle():
        print("❌ The book title Error")
        return

    author = input("Enter Author: ").strip()
    genre = input("Enter Genre: ").strip()

    try:
        price = float(input("Enter Price: ").strip())
        if price <= 0:
            print("❌ The price must be a positive number.")
            return
    except ValueError:
        print("❌ Invalid price format! Enter a valid number (e.g., 19.99).")
        return

    try:
        stock = int(input("Enter Stock Quantity: ").strip())
        if stock < 0:
            print("❌ The quantity must be a non-negative integer.")
            return
    except ValueError:
        print("❌ Invalid stock format! Enter a whole number (e.g., 10).")
        return

    # Create and add the book
    new_book = Book(isbn, title, author, genre, price, stock)
    bookstore.books.append(new_book)
    bookstore.save_books()
    print("✅ Book added successfully!")





    
    