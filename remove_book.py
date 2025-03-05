""" 
    1. remove book by the book id or isbn
    2. save it 
"""

from bookstore import BookStore
from book import Book


def remove_book(bookstore):
    print("\n--Remove a Book--")
    isbn = input("Enter ISBN of the book to remove: ").strip()

    for book in bookstore.books:
        if book.isbn == isbn:
            bookstore.books.remove(book)
            bookstore.save_books()
            print("Book removed successfully!")
            return

    print("Book not found!")
