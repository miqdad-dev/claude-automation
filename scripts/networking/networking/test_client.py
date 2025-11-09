import client
import unittest
from unittest.mock import Mock

class TestClient(unittest.TestCase):
    def setUp(self):
        self.mock_socket = Mock()
        self.client = client.Client(socket=self.mock_socket)

    def test_receive(self):
        self.mock_socket.recv.return_value = 'test message'
        self.client.receive()
        self.mock_socket.send.assert_called_with(self.client.nickname)

    def test_write(self):
        self.mock_socket.send.return_value = 'test message'
        self.client.write()
        self.mock_socket.send.assert_called_with(self.client.nickname + ': ' + 'test message')

if __name__ == '__main__':
    unittest.main()