from flask import Flask, request
from cryptography.fernet import Fernet

app = Flask(__name__)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(request.data)
    return {'key': key.decode(), 'encrypted_text': encrypted_text.decode()}

@app.route('/decrypt', methods=['POST'])
def decrypt():
    key = request.json['key']
    encrypted_text = request.json['encrypted_text']
    cipher_suite = Fernet(key.encode())
    decrypted_text = cipher_suite.decrypt(encrypted_text.encode())
    return {'decrypted_text': decrypted_text.decode()}