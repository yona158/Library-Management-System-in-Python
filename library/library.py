class Book:
    def __init__(self, id, title, author, quantity):
        self.id = id
        self.title = title
        self.author = author
        self.quantity = quantity

    def is_available(self):
        return self.quantity > 0

    def __str__(self):
        return (f"Book Details:\n"
                f"  ID: {self.id}\n"
                f"  Title: {self.title}\n"
                f"  Author: {self.author}\n"
                f"  Quantity: {self.quantity}\n"
                f"  Available: {'Yes' if self.is_available() else 'No'}")


class Library:
    def __init__(self):
        self.books = []  # List to store all books in the library
        self.borrowed_books_by_members = {}  # {book_id: [member_id1, member_id2]} - Tracks which members borrowed which books
        self.members = []  # List to store all members in the library

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book objects can be added to the library.")
        """Add a new book to the library."""
        self.books.append(book)
        print(f'"{book.title}" has been added')

    def remove_book(self, id):
        """Remove a book from the library by its ID."""
        for book in self.books:
            if book.id == id:
                self.books.remove(book)
                return f'"{book.title}" with id {id} has been removed'
        return f'We cannot find a book with id {id}'

    def search_for_book_by_title(self, name):
        """Search for books by title (case-insensitive)."""
        result = []
        for book in self.books:
            if name.lower() in book.title.lower():
                result.append(book)
        return result if result else ['No Books Found']

    def search_for_book_by_author(self, author):
        """Search for books by author (case-insensitive)."""
        result = []
        for book in self.books:
            if author.lower() in book.author.lower():
                result.append(book)
        return result if result else ['No Books Found']

    def borrow_book(self, book_id, member):
        """
        Allow a member to borrow a book.
        - Reduces the book's quantity by 1.
        - Adds the member to the book's borrower list.
        - Adds the book to the member's borrowed books list.
        """
        # Find the book by ID
        book = next((b for b in self.books if b.id == book_id), None)
        if book:
            if book.is_available():
                book.quantity -= 1  # Reduce quantity by 1
                # Add to borrowed_books_by_members
                if book_id in self.borrowed_books_by_members:
                    self.borrowed_books_by_members[book_id].append(member.member_id)
                else:
                    self.borrowed_books_by_members[book_id] = [member.member_id]
                # Add to member's list of borrowed books
                member.books_borrowed_by_member.append(book)
                print(f"Borrowed: {book.title}")
            else:
                print(f"No copies of {book.title} are available.")
        else:
            print(f"Book with id {book_id} not found.")

    def return_book(self, book_id, member):
        """
        Allow a member to return a book.
        - Increases the book's quantity by 1.
        - Removes the member from the book's borrower list.
        - Removes the book from the member's borrowed books list.
        """
        # Check if the book is borrowed by the member
        if book_id in self.borrowed_books_by_members and member.member_id in self.borrowed_books_by_members[book_id]:
            # Find the book by ID
            book = next((b for b in self.books if b.id == book_id), None)
            if book:
                book.quantity += 1  # Increase quantity by 1
                # Remove from borrowed_books_by_members
                self.borrowed_books_by_members[book_id].remove(member.member_id)
                if not self.borrowed_books_by_members[book_id]:  # If no more borrowers, remove the entry
                    del self.borrowed_books_by_members[book_id]
                # Remove from member's list of borrowed books
                member.books_borrowed_by_member = [b for b in member.books_borrowed_by_member if b.id != book_id]
                print(f"Returned: {book}")
        else:
            print(f"This book has not been borrowed by {member.name}.")

    def add_copies(self, id, quantity):
        """Add more copies of a book to the library."""
        for book in self.books:
            if book.id == id:
                book.quantity += quantity
                print(f"Added {quantity} copies of {book.title}. New quantity: {book.quantity}")
                return
        print(f"Book with id {id} not found.")

    def list_books(self):
        """Display all books in the library."""
        if not self.books:
            print("No Books In The Library.")
        else:
            print("Books:\n")
            for book in self.books:
                print(book)
                print('-' * 30)

    def show_all_borrowed_books(self):
        """Display all books currently borrowed and the members who borrowed them."""
        if not self.borrowed_books_by_members:
            print("No books are currently borrowed.")
        else:
            print("Borrowed Books:")
            for book_id, member_ids in self.borrowed_books_by_members.items():
                book = next((b for b in self.books if b.id == book_id), None)
                if book:
                    print(f"Book: {book.title} (ID: {book_id}) | Borrowed by Member IDs: {member_ids}")

    def show_members_who_borrowed_books(self):
        """Display all members who have borrowed books."""
        if not self.borrowed_books_by_members:
            print("No books are currently borrowed.")
        else:
            print("Members who borrowed books:")
            member_ids = set()  # Use a set to avoid duplicates
            for member_ids_list in self.borrowed_books_by_members.values():
                member_ids.update(member_ids_list)
            for member_id in member_ids:
                member = next((m for m in self.members if m.member_id == member_id), None)
                if member:
                    print(member)

    def show_all_members(self):
        """Display all members in the library."""
        if not self.members:
            print("No members in the library.")
        else:
            print("All Members:")
            for member in self.members:
                print(member)


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.books_borrowed_by_member = []  # List to store books borrowed by this member

    def __str__(self):
        return (f'Id : {self.member_id}\n'
                f'Name : {self.name}\n'
                f'Borrowed Books: {[book.title for book in self.books_borrowed_by_member] if self.books_borrowed_by_member else "No Borrowed Books"}')

    def list_borrowed_books(self):
        """Display all books borrowed by this member."""
        if not self.books_borrowed_by_member:
            print(f"{self.name} has no borrowed books.")
        else:
            print(f"{self.name}'s borrowed books:")
            for book in self.books_borrowed_by_member:
                print(book)
                print('-' * 30)