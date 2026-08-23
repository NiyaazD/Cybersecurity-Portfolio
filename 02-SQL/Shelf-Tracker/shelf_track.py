"""
Bookstore Database Program
Author: Your Name

This program allows the user to:
1. Add a new book
2. Update an author's details through a selected book
3. Delete a book
4. Search for books
5. Display all books with author information

Uses SQLite3 with parameterized queries to prevent SQL injection.
"""

import sqlite3


# -------------------------------------------------------
# DATABASE CONNECTION
# -------------------------------------------------------

def connect_database():
    """Create and return a database connection and cursor."""

    connection = sqlite3.connect("ebookstore.db")
    cursor = connection.cursor()
    return connection, cursor


# -------------------------------------------------------
# INPUT VALIDATION
# -------------------------------------------------------

def get_integer(message):
    """Ensure the user enters a valid integer."""

    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Please enter a valid number.")


def get_text(message):
    """Ensure text input is not empty."""

    while True:
        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty.")


# -------------------------------------------------------
# ENTER BOOK
# -------------------------------------------------------

def enter_book(connection, cursor):

    try:
        book_id = get_integer("Book ID: ")
        title = get_text("Title: ")
        author_id = get_integer("Author ID: ")
        quantity = get_integer("Quantity: ")

        cursor.execute(
            "INSERT INTO book VALUES (?, ?, ?, ?)",
            (book_id, title, author_id, quantity)
        )

        connection.commit()

        print("Book added successfully.")

    except sqlite3.Error as error:
        print("Database Error:", error)


# -------------------------------------------------------
# UPDATE BOOK
# -------------------------------------------------------

def update_book(connection, cursor):

    try:

        book_id = get_integer("Enter Book ID to update: ")

        cursor.execute("""
            SELECT book.title,
                   author.id,
                   author.name,
                   author.country
            FROM book
            INNER JOIN author
            ON book.authorID = author.id
            WHERE book.id = ?
        """, (book_id,))

        result = cursor.fetchone()

        if result:

            print("\nCurrent Details")
            print("--------------------------")
            print("Title:", result[0])
            print("Author:", result[2])
            print("Country:", result[3])

            new_name = get_text("Enter new author name: ")
            new_country = get_text("Enter new country: ")

            cursor.execute("""
                UPDATE author
                SET name = ?, country = ?
                WHERE id = ?
            """, (new_name, new_country, result[1]))

            connection.commit()

            print("Author updated successfully.")

        else:
            print("Book not found.")

    except sqlite3.Error as error:
        print("Database Error:", error)


# -------------------------------------------------------
# DELETE BOOK
# -------------------------------------------------------

def delete_book(connection, cursor):

    try:

        book_id = get_integer("Book ID to delete: ")

        cursor.execute(
            "DELETE FROM book WHERE id=?",
            (book_id,)
        )

        connection.commit()

        if cursor.rowcount == 0:
            print("Book not found.")
        else:
            print("Book deleted successfully.")

    except sqlite3.Error as error:
        print("Database Error:", error)


# -------------------------------------------------------
# SEARCH BOOK
# -------------------------------------------------------

def search_books(cursor):

    try:

        search = input("Enter Book ID or Title: ").strip()

        if search.isdigit():

            cursor.execute(
                "SELECT * FROM book WHERE id=?",
                (int(search),)
            )

        else:

            cursor.execute(
                "SELECT * FROM book WHERE title LIKE ?",
                ('%' + search + '%',)
            )

        books = cursor.fetchall()

        if books:

            print("\nResults")

            for book in books:

                print("-" * 40)
                print(f"ID: {book[0]}")
                print(f"Title: {book[1]}")
                print(f"Author ID: {book[2]}")
                print(f"Quantity: {book[3]}")

        else:
            print("No books found.")

    except sqlite3.Error as error:
        print("Database Error:", error)


# -------------------------------------------------------
# VIEW ALL BOOKS
# -------------------------------------------------------

def view_books(cursor):

    try:

        cursor.execute("""
            SELECT book.title,
                   author.name,
                   author.country
            FROM book
            INNER JOIN author
            ON book.authorID = author.id
        """)

        books = cursor.fetchall()

        print("\nBook Details")

        for title, author, country in books:

            print("-" * 50)
            print("Title:", title)
            print("Author:", author)
            print("Country:", country)

        print("-" * 50)

    except sqlite3.Error as error:
        print("Database Error:", error)


# -------------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------------

def main():

    try:

        connection, cursor = connect_database()

        while True:

            print("\nBOOKSTORE MENU")
            print("1. Enter book")
            print("2. Update book")
            print("3. Delete book")
            print("4. Search books")
            print("5. View details of all books")
            print("0. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                enter_book(connection, cursor)

            elif choice == "2":
                update_book(connection, cursor)

            elif choice == "3":
                delete_book(connection, cursor)

            elif choice == "4":
                search_books(cursor)

            elif choice == "5":
                view_books(cursor)

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")

    except sqlite3.Error as error:
        print("Unable to connect to the database:", error)

    finally:
        connection.close()
        print("Database connection closed.")


# -------------------------------------------------------
# PROGRAM ENTRY POINT
# -------------------------------------------------------

if __name__ == "__main__":
    main()