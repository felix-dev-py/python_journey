import sqlite3

conn = sqlite3.connect("test.db")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER NOT NULL
    )
""")

def add_book(cursor, title, author, year):
    this_cursor = cursor
    data_tuple = (title, author, year)
    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", data_tuple)

def show_books(cursor):
    this_cursor = cursor
    this_cursor.execute("SELECT * FROM books")
    return this_cursor.fetchall()

def find_books_by_author(cursor, author):
    this_cursor = cursor
    this_cursor.execute("SELECT * FROM books WHERE author = ?", (author,))
    return this_cursor.fetchall()

add_book(cursor, "First", "Frist_author", 2001)
add_book(cursor, "Second", "Second_author", 2002)
add_book(cursor, "Third", "Third_author", 2003)

data = show_books(cursor)
for i in data:
    print(i)

print("--------------")

data2 = find_books_by_author(cursor, "Third_author")
for i in data2:
    print(i)

conn.commit()

conn.close()