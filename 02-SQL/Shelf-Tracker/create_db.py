import sqlite3

conn = sqlite3.connect("ebookstore.db")
cursor = conn.cursor()

# Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS book (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    authorID INTEGER NOT NULL,
    qty INTEGER NOT NULL
)
""")

# Clear existing records (optional)
cursor.execute("DELETE FROM book")

# Insert the required books
books = [
    (3001, "A Tale of Two Cities", 1290, 30),
    (3002, "Harry Potter and the Philosopher's Stone", 8937, 40),
    (3003, "The Lion, the Witch and the Wardrobe", 2356, 25),
    (3004, "The Lord of the Rings", 6380, 37),
    (3005, "Alice's Adventures in Wonderland", 5620, 12)
]

cursor.executemany(
    "INSERT INTO book VALUES (?, ?, ?, ?)",
    books
)

# Create author table
cursor.execute("""
CREATE TABLE IF NOT EXISTS author (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    country TEXT NOT NULL
)
""")

# Clear existing records
cursor.execute("DELETE FROM author")

# Insert authors
authors = [
    (1290, "Charles Dickens", "England"),
    (8937, "J.K. Rowling", "England"),
    (2356, "C.S. Lewis", "Ireland"),
    (6380, "J.R.R. Tolkien", "South Africa"),
    (5620, "Lewis Carroll", "England")
]

cursor.executemany(
    "INSERT INTO author VALUES (?, ?, ?)",
    authors
)

conn.commit()
conn.close()

print("Database created successfully.")