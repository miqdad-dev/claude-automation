import unittest
from server import Server
from client import Client
import threading

class TestChatApp(unittest.TestCase):
    def test_server_creation(self):
        server = Server('127.0.0.1', 55555)
        self.assertEqual(server.host, '127.0.0.1')
        self.assertEqual(server.port, 55555)

    def test_client_creation(self):
        client = Client('Test', '127.0.0.1', 55555)
        self.assertEqual(client.nickname, 'Test')

if __name__ == "__main__":
    unittest.main()