import unittest
from server import Server
from client import client, nickname

class TestServer(unittest.TestCase):
    def setUp(self):
        self.server = Server('127.0.0.1', 55555)

    def test_broadcast(self):
        self.server.clients.append(client)
        self.server.broadcast('test'.encode('ascii'))
        self.assertEqual(client.recv(1024).decode('ascii'), 'test')

    def test_handle(self):
        self.server.clients.append(client)
        client.send(f'{nickname}: test'.encode('ascii'))
        self.assertEqual(self.server.handle(client), f'{nickname}: test')

if __name__ == '__main__':
    unittest.main()