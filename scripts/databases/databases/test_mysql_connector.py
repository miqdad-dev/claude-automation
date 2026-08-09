import unittest
from mysql_connector import create_connection

class TestMysqlConnector(unittest.TestCase):
    def test_create_connection(self):
        connection = create_connection("db", "root", "password")
        self.assertIsNotNone(connection)

if __name__ == '__main__':
    unittest.main()