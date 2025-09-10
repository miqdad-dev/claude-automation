import sqlite3
import main

def test_add_and_list_books():
    connection = sqlite3.connect(':memory:')
    main.create_table(connection)
    main.add_book(connection, '1984', 'George Orwell', 1949)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books')
    rows = cursor.fetchall()
    assert rows == [(1, '1984', 'George Orwell', 1949)]

def test_delete_book():
    connection = sqlite3.connect(':memory:')
    main.create_table(connection)
    main.add_book(connection, '1984', 'George Orwell', 1949)
    main.delete_book(connection, 1)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books')
    rows = cursor.fetchall()
    assert rows == []