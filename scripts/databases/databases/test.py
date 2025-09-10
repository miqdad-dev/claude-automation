import unittest
import os
import sqlite3
from main import create_database, create_table, insert_record

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db_name = "test.db"
        self.conn = sqlite3.connect(self.db_name)

    def tearDown(self):
        self.conn.close()
        os.remove(self.db_name)

    def test_create_database(self):
        create_database("test2.db")
        self.assertTrue(os.path.exists("test2.db"))
        os.remove("test2.db")

    def test_create_table(self):
        create_table(self.conn, "users", "id INT, name TEXT")
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        self.assertIsNotNone(cursor.fetchone())

    def test_insert_record(self):
        create_table(self.conn, "users", "id INT, name TEXT")
        insert_record(self.conn, "users", "id, name", "1, 'John Doe'")
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id=1")
        self.assertIsNotNone(cursor.fetchone())

if __name__ == "__main__":
    unittest.main()