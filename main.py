
from bookstore import BookStore
from add_book import add_book
from view_books import view_books
from search_book import search_book
from remove_book import remove_book


def main():
    bookstore = BookStore()

    while True:
        print("\n====================================================")
        print("\n-------------Book Store Management System-----------")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(bookstore)
        elif choice == "2":
            view_books(bookstore)
        elif choice == "3":
            search_book(bookstore)
        elif choice == "4":
            remove_book(bookstore)
        elif choice == "5":
            print("\n🚪 Exiting... See you next time! 👋\n")
            break
        else:
            print("Invalid choice! Please enter a number between 1-5.")

if __name__ == "__main__":
    main()
