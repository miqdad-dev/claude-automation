import server
import unittest
from unittest.mock import Mock

class TestServer(unittest.TestCase):
    def setUp(self):
        self.mock_socket = Mock()
        self.server = server.Server(socket=self.mock_socket)

    def test_broadcast(self):
        self.mock_socket.recv.return_value = 'test message'
        self.server.broadcast('test message')
        self.mock_socket.send.assert_called_with('test message')

    def test_handle(self):
        self.mock_socket.recv.side_effect = ['message', 'quit']
        self.server.handle(self.mock_socket)
        self.mock_socket.send.assert_called_with('quit')

if __name__ == '__main__':
    unittest.main()