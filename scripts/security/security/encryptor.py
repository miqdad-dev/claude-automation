import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

class Encryptor:

    def __init__(self, password: str):
        self.password = password

    def generate_key(self):
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.password))
        return key

    def encrypt_text(self, text: str):
        key = self.generate_key()
        f = Fernet(key)
        encrypted_text = f.encrypt(text)
        return encrypted_text

    def decrypt_text(self, encrypted_text: str):
        key = self.generate_key()
        f = Fernet(key)
        decrypted_text = f.decrypt(encrypted_text)
        return decrypted_text