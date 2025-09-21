import unittest
import server

class TestServer(unittest.TestCase):

    def test_handle_connection(self):
        response = server.handle_connection('Hello, Server!')
        self.assertEqual(response, 'Message received!')

if __name__ == '__main__':
    unittest.main()