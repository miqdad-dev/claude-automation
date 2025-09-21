import unittest
import client

class TestClient(unittest.TestCase):

    def test_send_message(self):
        response = client.send_message('Hello, Server!')
        self.assertEqual(response, 'Message received!')

if __name__ == '__main__':
    unittest.main()