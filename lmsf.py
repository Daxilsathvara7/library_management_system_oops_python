class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {'Yes' if self.available else 'No'}")

    def mark_as_borrowed(self):
        self.available = False

    def mark_as_returned(self):
        self.available = True

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def display_details(self):
        print(f"Name: {self.name}, Member ID: {self.member_id}")
        if self.borrowed_books:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print(f"- {book.title}")
        else:
            print("No books currently borrowed.")

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.mark_as_borrowed()
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.mark_as_returned()
            return True
        return False

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' has been added to the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' has been added to the library.")

    def display_books(self):
        print(f"Books available in {self.name}:")
        for book in self.books:
            if book.available:
                book.display_details()

    def display_members(self):
        print(f"Members of {self.name}:")
        for member in self.members:
            member.display_details()

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None


def get_valid_input(prompt, valid_options=None):
    while True:
        user_input = input(prompt).strip()
        if valid_options is None or user_input in valid_options:
            return user_input
        print("Invalid input. Please try again.")


if __name__ == '__main__':
    library = Library("my Library")

    library.add_book(Book("b1", "a1", "1"))
    library.add_book(Book("b2", "a2", "2"))
    library.add_book(Book("b3", "a3", "3"))

    library.add_member(Member("ab", "1"))
    library.add_member(Member("cd", "2"))

    while True:
        print(f"\nWelcome to the {library.name}. Enter your choice to continue:")
        print("1. Display Available Books")
        print("2. Display Members")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Exit")

        choice = get_valid_input("Enter your choice (1-5): ", ['1', '2', '3', '4', '5'])

        if choice == '1':
            library.display_books()

        elif choice == '2':
            library.display_members()

        elif choice == '3':
            member_id = input("Enter member ID: ")
            member = library.find_member(member_id)
            if member:
                book_title = input("Enter the title of the book you want to borrow: ")
                book = library.find_book(book_title)
                if book:
                    if member.borrow_book(book):
                        print(f"Successfully borrowed '{book.title}'.")
                    else:
                        print("Sorry, this book is not available.")
                else:
                    print("Book not found in the library.")
            else:
                print("Member not found.")

        elif choice == '4':
            member_id = input("Enter member ID: ")
            member = library.find_member(member_id)
            if member:
                book_title = input("Enter the title of the book you want to return: ")
                book = library.find_book(book_title)
                if book:
                    if member.return_book(book):
                        print(f"Successfully returned '{book.title}'.")
                    else:
                        print("You didn't borrow this book from our library.")
                else:
                    print("Book not found in the library.")
            else:
                print("Member not found.")

        elif choice == '5':
            print("Thank you for using the library system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

        input("\nPress Enter to continue...")
