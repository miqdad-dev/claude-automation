import sqlite3
import sys

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER)')
    connection.commit()

def add_book(connection, title, author, year):
    cursor = connection.cursor()
    cursor.execute('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', (title, author, year))
    connection.commit()

def list_books(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def delete_book(connection, book_id):
    cursor = connection.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    connection.commit()

def main():
    connection = sqlite3.connect('books.db')
    while True:
        print('1. Create table')
        print('2. Add book')
        print('3. List books')
        print('4. Delete book')
        print('5. Quit')
        choice = input('Choose an option: ')
        if choice == '1':
            create_table(connection)
        elif choice == '2':
            title = input('Enter book title: ')
            author = input('Enter author name: ')
            year = int(input('Enter year of publication: '))
            add_book(connection, title, author, year)
        elif choice == '3':
            list_books(connection)
        elif choice == '4':
            book_id = int(input('Enter the id of the book to delete: '))
            delete_book(connection, book_id)
        elif choice == '5':
            break

if __name__ == '__main__':
    main()