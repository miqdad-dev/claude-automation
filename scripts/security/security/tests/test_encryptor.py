import unittest
from encryptor import Encryptor

class EncryptorTest(unittest.TestCase):

    def setUp(self):
        self.encryptor = Encryptor("password")

    def test_encryption_decryption(self):
        text = "Hello, World!"
        encrypted_text = self.encryptor.encrypt_text(text)
        decrypted_text = self.encryptor.decrypt_text(encrypted_text)
        self.assertEqual(text, decrypted_text)

if __name__ == '__main__':
    unittest.main()