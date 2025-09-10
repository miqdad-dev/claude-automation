import sqlite3
import os

def create_database(name):
    conn = sqlite3.connect(name)
    conn.close()

def create_table(conn, name, columns):
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE {name} ({columns})")
    conn.commit()

def insert_record(conn, table, columns, values):
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {table} ({columns}) VALUES ({values})")
    conn.commit()

def menu():
    print("1. Create database")
    print("2. Select database")
    print("3. Quit")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Enter database name: ")
        create_database(name)
    elif choice == "2":
        name = input("Enter database name: ")
        if os.path.exists(name):
            conn = sqlite3.connect(name)
            table_menu(conn)
        else:
            print("Database does not exist.")
    elif choice == "3":
        exit()

def table_menu(conn):
    print("1. Create table")
    print("2. Select table")
    print("3. Back")
    choice = input("Enter choice: ")
    if choice == "1":
        name = input("Enter table name: ")
        columns = input("Enter columns (comma-separated): ")
        create_table(conn, name, columns)
    elif choice == "2":
        name = input("Enter table name: ")
        record_menu(conn, name)
    elif choice == "3":
        menu()

def record_menu(conn, table):
    print("1. Insert record")
    print("2. Select record")
    print("3. Delete record")
    print("4. Back")
    choice = input("Enter choice: ")
    if choice == "1":
        columns = input("Enter column names (comma-separated): ")
        values = input("Enter values (comma-separated): ")
        insert_record(conn, table, columns, values)
    elif choice == "4":
        table_menu(conn)

if __name__ == "__main__":
    while True:
        menu()