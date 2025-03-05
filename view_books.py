""" 
    1. View all the books
"""

from bookstore import BookStore
from add_book import add_book


def view_books(bookstore):
    print("\n--Available Books--")
    if not bookstore.books:
        print("No books available!")
        return

    print(f"{'ISBN':<15}{'Title':<30}{'Author':<20}{'Genre':<15}{'Price':<10}{'Stock'}")
    print("-" * 90)

    for book in bookstore.books:
        print(f"{book.isbn:<15}{book.title[:30]:<30}{book.author[:20]:<20}{book.genre:<15}{book.price:<10}{book.stock}")

