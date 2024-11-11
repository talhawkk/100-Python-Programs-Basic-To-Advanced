class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"Sorry, {book.title} is currently unavailable.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print(f"{self.name} does not have {book.title} borrowed.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed:")
            for book in self.borrowed_books:
                print(f" - {book.title}")
        else:
            print(f"{self.name} has not borrowed any books.")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} to the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Added member {member.name}.")

    def list_available_books(self):
        print("Available Books:")
        for book in self.books:
            if book.is_available:
                print(f" - {book}")

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None


library = Library()
book1 = Book("python for data science", "xyz", "1234567890")
book2 = Book("Python", "abc", "2345678901")
library.add_book(book1)
library.add_book(book2)

member1 = Member(1, "Talha")
library.add_member(member1)

library.list_available_books()

member1.borrow_book(book1)
library.list_available_books()

member1.return_book(book1)
library.list_available_books()
