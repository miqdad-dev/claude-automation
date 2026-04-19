import unittest
import main
import json

class TestEncryption(unittest.TestCase):

    def setUp(self):
        self.app = main.app.test_client()
        self.app.testing = True

    def test_encrypt_decrypt(self):
        response = self.app.post('/encrypt', data=b'test')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(data['key'])
        self.assertIsNotNone(data['encrypted_text'])

        response = self.app.post('/decrypt', json={'key': data['key'], 'encrypted_text': data['encrypted_text']})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['decrypted_text'], 'test')

if __name__ == "__main__":
    unittest.main()