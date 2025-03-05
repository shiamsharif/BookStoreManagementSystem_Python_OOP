""" 
    1. Search boom by this id, title or author
    2. show the book
"""

from bookstore import BookStore
from book import Book


def search_book(bookstore):
    print("\n--- Search Book ---")
    query = input("Enter ISBN, Title, or Author: ").strip().lower()

    for book in bookstore.books:
        if query in book.isbn.lower() or query in book.title.lower() or query in book.author.lower():
            print("\nBook Found:")
            print("ISBN | Title | Author | Genre | Price | Stock")
            print(book.to_string().strip())
            return

    print("No matching book found!!!!!!!")
