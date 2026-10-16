from abc import ABC, abstractmethod
from datetime import datetime

# ------------------ ABSTRACT CLASS ------------------
class Person(ABC):
    def __init__(self, name, user_id):
        self._name = name
        self._user_id = user_id

    @abstractmethod
    def display_role(self):
        pass


# ------------------ USER CLASS ------------------
class User(Person):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.borrowed_books = []

    def display_role(self):
        return "User"

    def borrow_book(self, book, library):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            library.transactions.append(Transaction(self, book))
            print(f"{self._name} borrowed {book.title}")
        else:
            print("Book not available!")

    def return_book(self, book, library):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)

            # Calculate fine
            for t in library.transactions:
                if t.book == book and t.user == self and not t.returned:
                    t.return_book()
                    print(f"{self._name} returned {book.title}")
                    if t.fine > 0:
                        print(f"Fine: ₹{t.fine}")
                    return
        else:
            print("This book was not borrowed by you.")


# ------------------ ADMIN CLASS ------------------
class Admin(Person):
    def display_role(self):
        return "Admin"

    def add_book(self, library, book):
        library.books.append(book)
        print(f"Book '{book.title}' added.")

    def remove_book(self, library, book_id):
        for book in library.books:
            if book.book_id == book_id:
                library.books.remove(book)
                print("Book removed.")
                return
        print("Book not found.")

# ------------------ BOOK CLASS ------------------
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"{self.book_id} | {self.title} | {self.author} | {status}"


# ------------------ TRANSACTION CLASS ------------------
class Transaction:
    def __init__(self, user, book):
        self.user = user
        self.book = book
        self.issue_date = datetime.now()
        self.return_date = None
        self.returned = False
        self.fine = 0

    def return_book(self):
        self.return_date = datetime.now()
        self.returned = True

        # Fine logic (₹10 per day after 7 days)
        days = (self.return_date - self.issue_date).days
        if days > 7:
            self.fine = (days - 7) * 10


# ------------------ LIBRARY CLASS ------------------
class Library:
    def __init__(self):
        self.books = []
        self.transactions = []

    def show_books(self):
        for book in self.books:
            print(book)

    def search_book(self, keyword):
        for book in self.books:
            if keyword.lower() in book.title.lower():
                print(book)
            else:
                print("No Book FOund")


# ------------------ MAIN PROGRAM ------------------
def main():
    library = Library()

    admin = Admin("Admin", 1)
    user = User("Kartiki", 101)

    # Add books
    admin.add_book(library, Book(1, "Python Basics", "John"))
    admin.add_book(library, Book(2, "OOP Concepts", "Smith"))

    while True:
        print("\n1. Show Books\n2. Search Book\n3. Borrow\n4. Return\n5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            library.show_books()

        elif choice == "2":
            keyword = input("Enter title keyword: ")
            library.search_book(keyword)

        elif choice == "3":
            book_id = int(input("Enter book ID: "))
            for book in library.books:
                if book.book_id == book_id:
                    user.borrow_book(book, library)

        elif choice == "4":
            book_id = int(input("Enter book ID: "))
            for book in library.books:
                if book.book_id == book_id:
                    user.return_book(book, library)

        elif choice == "5":
            print("Thank You For Using Our Book Library!!!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()