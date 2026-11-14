# ==========================================
#       LIBRARY MANAGEMENT SYSTEM
# ==========================================


class Book:
    """Represents a single book in the library."""

    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity          # Total number of copies
        self.available = quantity         # Currently available copies
        self.issued_to = []               # List of students holding copies

    def display(self):
        """Display book information."""
        print(f"\nBook ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Total Quantity: {self.quantity}")
        print(f"Available Quantity: {self.available}")
        print(f"Issued Copies: {len(self.issued_to)}")


class Library:
    """Manages all library operations."""

    def __init__(self):
        # Dictionary used to store books
        # Key = Book ID, Value = Book object
        self.books = {}

    def add_book(self):
        """Add a new book to the library."""
        print("\n===== ADD NEW BOOK =====")

        book_id = input("Enter Book ID: ").strip()

        # Check for unique Book ID
        if book_id in self.books:
            print("Error: A book with this ID already exists!")
            return

        title = input("Enter Book Title: ").strip()
        author = input("Enter Author Name: ").strip()

        # Validate quantity
        try:
            quantity = int(input("Enter Quantity: ").strip())

            if quantity <= 0:
                print("Error: Quantity must be a positive whole number!")
                return

        except ValueError:
            print("Error: Please enter a valid whole number for quantity!")
            return

        # Create Book object and add it to dictionary
        new_book = Book(book_id, title, author, quantity)
        self.books[book_id] = new_book

        print("\nBook added successfully!")

    def view_all_books(self):
        """Display all books in the library."""
        print("\n===== ALL BOOKS =====")

        if not self.books:
            print("No books are available in the library.")
            return

        print("-" * 75)
        print(f"{'ID':<10}{'Title':<25}{'Author':<20}{'Available':<10}")
        print("-" * 75)

        for book in self.books.values():
            print(
                f"{book.book_id:<10}"
                f"{book.title:<25}"
                f"{book.author:<20}"
                f"{book.available:<10}"
            )

        print("-" * 75)

    def search_book(self):
        """Search for a book by ID or title."""
        print("\n===== SEARCH BOOK =====")

        if not self.books:
            print("No books are available in the library.")
            return

        search = input("Enter Book ID or Title: ").strip().lower()

        found_books = []

        for book in self.books.values():
            if (search == book.book_id.lower() or
                    search in book.title.lower()):
                found_books.append(book)

        if found_books:
            print(f"\n{len(found_books)} book(s) found:")

            for book in found_books:
                book.display()
        else:
            print("Book not found!")

    def issue_book(self):
        """Issue an available book to a student."""
        print("\n===== ISSUE BOOK =====")

        book_id = input("Enter Book ID: ").strip()

        # Check whether book exists
        if book_id not in self.books:
            print("Book not found!")
            return

        book = self.books[book_id]

        # Check availability
        if book.available <= 0:
            print("Sorry! No copies of this book are currently available.")
            return

        student_name = input("Enter Student Name: ").strip()

        if not student_name:
            print("Student name cannot be empty!")
            return

        # Issue the book
        book.available -= 1
        book.issued_to.append(student_name)

        print("\nBook issued successfully!")
        print(f"Student: {student_name}")
        print(f"Available Quantity: {book.available}")

    def return_book(self):
        """Return a book issued to a student."""
        print("\n===== RETURN BOOK =====")

        book_id = input("Enter Book ID: ").strip()

        # Check whether book exists
        if book_id not in self.books:
            print("Book not found!")
            return

        book = self.books[book_id]

        student_name = input("Enter Student Name: ").strip()

        # Check whether this student has issued the book
        if student_name not in book.issued_to:
            print("No matching issued record found for this student!")
            return

        # Return the book
        book.issued_to.remove(student_name)
        book.available += 1

        print("\nBook returned successfully!")
        print(f"Available Quantity: {book.available}")

    def delete_book(self):
        """Delete a book only if no copies are issued."""
        print("\n===== DELETE BOOK =====")

        book_id = input("Enter Book ID: ").strip()

        # Check whether book exists
        if book_id not in self.books:
            print("Book not found!")
            return

        book = self.books[book_id]

        # A book cannot be deleted while issued
        if len(book.issued_to) > 0:
            print("Cannot delete this book because copies are currently issued!")
            return

        del self.books[book_id]

        print("Book deleted successfully!")

    def view_issued_books(self):
        """Display all currently issued books."""
        print("\n===== ISSUED BOOKS =====")

        issued_found = False

        for book in self.books.values():
            if book.issued_to:
                issued_found = True

                for student in book.issued_to:
                    print(f"\nBook ID: {book.book_id}")
                    print(f"Title: {book.title}")
                    print(f"Student: {student}")
                    print("-" * 30)

        if not issued_found:
            print("No books are currently issued.")


def display_menu():
    """Display the main menu."""
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. View Issued Books")
    print("8. Exit")


def main():
    """Main function that runs the Library Management System."""

    # Create a Library object
    library = Library()

    # Keep the program running until the user exits
    while True:
        display_menu()

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            library.add_book()

        elif choice == "2":
            library.view_all_books()

        elif choice == "3":
            library.search_book()

        elif choice == "4":
            library.issue_book()

        elif choice == "5":
            library.return_book()

        elif choice == "6":
            library.delete_book()

        elif choice == "7":
            library.view_issued_books()

        elif choice == "8":
            print("\nThank you for using the Library Management System!")
            print("Program closed safely.")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 8.")


# Program starts here
if __name__ == "__main__":
    main()