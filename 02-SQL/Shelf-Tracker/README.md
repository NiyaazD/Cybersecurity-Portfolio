# Shelf Tracker

## Overview

Shelf Tracker is a command-line bookstore inventory management application developed as part of my HyperionDev Cyber Security Bootcamp.

The application connects to an SQLite database and allows users to manage a bookstore's inventory through an interactive menu-driven interface. Users can add books, update author information, search inventory, delete books, and display all stored records.

The project demonstrates practical database management using Python and SQLite while following secure coding practices such as parameterized SQL queries and input validation.

---

## Features

- Add new books to the database
- Update author information for existing books
- Delete books from the inventory
- Search books by ID or title
- Display all books with author details
- Uses INNER JOIN to retrieve related data
- Input validation for numeric and text fields
- Error handling for database operations
- Menu-driven command-line interface

---

## Technologies Used

- Python 3
- SQLite3
- SQL
- Object-Oriented Programming principles
- Parameterized SQL queries

---

## Database Structure

The application uses two related tables:

### Book Table

| Field | Description |
|-------|-------------|
| ID | Book identifier |
| Title | Book title |
| AuthorID | Foreign key linking to Author |
| Quantity | Number of books in stock |

### Author Table

| Field | Description |
|-------|-------------|
| ID | Author identifier |
| Name | Author name |
| Country | Author country |

The relationship between the tables is managed using SQL INNER JOIN queries.

---

## How to Run

1. Ensure Python 3 is installed.
2. Create the database by running:

```bash
python create_db.py
```

3. Run the application:

```bash
python shelf_track.py
```

---

## Example Menu

```
BOOKSTORE MENU

1. Enter book
2. Update book
3. Delete book
4. Search books
5. View details of all books
0. Exit
```

---

## Skills Demonstrated

- SQLite database management
- CRUD operations
- SQL JOIN queries
- Database normalization concepts
- Python functions
- Modular programming
- Exception handling
- User input validation
- Secure database programming using parameterized queries

---

## Learning Outcomes

Through this project I gained practical experience with:

- Designing relational databases
- Connecting Python applications to SQLite databases
- Managing database records programmatically
- Writing secure SQL queries
- Building interactive command-line applications
- Structuring larger Python programs using reusable functions

---

## Future Improvements

Possible enhancements include:

- Add book editing functionality
- Search by author name
- Display low-stock alerts
- Export inventory reports
- Graphical user interface (GUI)
- User authentication and role-based access
- Logging of inventory changes

---

**Author:** Niyaaz Dawjee