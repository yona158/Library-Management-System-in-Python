from library import Book, Library, Member

# CLI Implementation
def cli(library):
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book by Title")
        print("4. Search Book by Author")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Add Copies of a Book")
        print("8. List All Books")
        print("9. Show All Borrowed Books")
        print("10. Show Members Who Borrowed Books")
        print("11. Show All Members")
        print("12. Add Member")
        print("13. List Borrowed Books by a Member")
        print("14. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add Book
            id = int(input("Enter book ID: "))
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            quantity = int(input("Enter book quantity: "))
            library.add_book(Book(id, title, author, quantity))

        elif choice == "2":
            # Remove Book
            id = int(input("Enter book ID to remove: "))
            print(library.remove_book(id))

        elif choice == "3":
            # Search Book by Title
            title = input("Enter book title to search: ")
            results = library.search_for_book_by_title(title)
            for book in results:
                print(book)

        elif choice == "4":
            # Search Book by Author
            author = input("Enter book author to search: ")
            results = library.search_for_book_by_author(author)
            for book in results:
                print(book)

        elif choice == "5":
            # Borrow Book
            book_id = int(input("Enter book ID to borrow: "))
            member_id = int(input("Enter member ID: "))
            member = next((m for m in library.members if m.member_id == member_id), None)
            if member:
                library.borrow_book(book_id, member)
            else:
                print("Member not found.")

        elif choice == "6":
            # Return Book
            book_id = int(input("Enter book ID to return: "))
            member_id = int(input("Enter member ID: "))
            member = next((m for m in library.members if m.member_id == member_id), None)
            if member:
                library.return_book(book_id, member)
            else:
                print("Member not found.")

        elif choice == "7":
            # Add Copies of a Book
            id = int(input("Enter book ID to add copies: "))
            quantity = int(input("Enter number of copies to add: "))
            library.add_copies(id, quantity)

        elif choice == "8":
            # List All Books
            library.list_books()

        elif choice == "9":
            # Show All Borrowed Books
            library.show_all_borrowed_books()

        elif choice == "10":
            # Show Members Who Borrowed Books
            library.show_members_who_borrowed_books()

        elif choice == "11":
            # Show All Members
            library.show_all_members()

        elif choice == "12":
            # Add Member
            name = input("Enter member name: ")
            member_id = int(input("Enter member ID: "))
            member = Member(name, member_id)
            library.members.append(member)
            print(f"Member {name} with ID {member_id} added successfully.")

        elif choice == "13":
            # List Borrowed Books by a Member
            member_id = int(input("Enter member ID: "))
            member = next((m for m in library.members if m.member_id == member_id), None)
            if member:
                member.list_borrowed_books()
            else:
                print("Member not found.")

        elif choice == "14":
            # Exit
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Main Program
if __name__ == "__main__":
    library = Library()
    cli(library)