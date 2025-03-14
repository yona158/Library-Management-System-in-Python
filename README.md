# Library-Management-System-in-Python
A **command-line interface (CLI)** based Library Management System built using Python. This project is designed to help librarians manage books and members efficiently. It provides a user-friendly interface for adding, removing, searching, and tracking books, as well as managing members and their borrowed books.

## Features  
### Book Management
- **Add Books:** Add new books to the library by providing details like ID, title, author, and quantity.
- **Remove Books:** Remove books from the library using their unique ID.
- **Search Books:** Search for books by title or author (case-insensitive).
- **Update Quantity:** Add more copies of an existing book to the library.
-  **Check Availability:** View whether a book is available for borrowing.

### Member Management
**Add Members:** Register new members with a name and unique member ID.
**Borrow Books:** Allow members to borrow available books. The system automatically updates the book's quantity.
**Return Books:** Allow members to return borrowed books. The system updates the book's quantity and removes it from the member's borrowed list.
**Track Borrowed Books:** View all books borrowed by a specific member.

### Reporting
**List All Books:** Display details of all books in the library, including availability.
**View Borrowed Books:** Show all books currently borrowed and the members who borrowed them.
**List All Members:** Display all registered members and the books they have borrowed.

## How It Works
The system is built using **object-oriented programming (OOP)** principles, making it modular and easy to extend. It consists of three main classes:
**1-Book Class:**
- Represents a book with attributes like id, title, author, and quantity.
- Includes methods like is_available() to check if a book is in stock.

**2-Member Class:**
-Represents a library member with attributes like name, member_id, and books_borrowed_by_member.
-Includes methods to list all books borrowed by the member.

**3-Library Class:**
-Manages the collection of books and members.
-Handles operations like adding/removing books, borrowing/returning books, and generating reports.

The **CLI** provides an interactive menu for users to perform these operations easily.

## Installation
1-Clone the repository:
`git clone https://github.com/your-username/library-management-system.git`

2-Navigate to the project directory:
`cd library-management-system`

3-Run the program:
`python main.py`

## Usage
### Main Menu
The CLI provides the following options:
**1- Add Book:** Add a new book to the library.
**2- Remove Book:** Remove a book by its ID.
**3- Search Book by Title:** Search for books by title.
**4- Search Book by Author:** Search for books by author.
**5- Borrow Book:** Allow a member to borrow a book.
**6- Return Book:** Allow a member to return a book.
**7- Add Copies**: Add more copies of an existing book.
**8- List All Books:** Display all books in the library.
**9- Show Borrowed Books:** Display all currently borrowed books.
**10- Show Members Who Borrowed Books:** Display members who have borrowed books.
**11- Show All Members:** Display all registered members.
**12- Add Member**: Register a new member.
**13- List Borrowed Books by Member:** Display books borrowed by a specific member.
**14- Exit:** Exit the program.

## Future Enhancements
- Graphical User Interface (GUI): Implement a GUI using Tkinter or PyQt for a more user-friendly experience.
- Database Integration: Use SQLite or MySQL to store book and member data persistently.
- User Authentication: Add login functionality for librarians and members.
- Advanced Search: Implement advanced search options (e.g., by genre, publication year).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions, feedback, or collaborations, feel free to reach out:
**Email:** [bayan.jess998@gmail.com]
**GitHub:** yona158

