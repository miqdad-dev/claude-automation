# Password-based Encryption-Decryption Tool

This tool uses a password-based key derivation function to encrypt and decrypt text.

## How it works

- The tool uses the PBKDF2HMAC key derivation function from the Cryptography library in Python.
- The key derivation function uses a random salt, the SHA256 algorithm, and 100000 iterations to derive a key from the password.
- The derived key is then used to encrypt and decrypt text using the Fernet symmetric encryption scheme.

## How to run

1. Clone the repository.
2. Install the necessary dependencies with `pip install -r requirements.txt`.
3. Run the tests with `python -m unittest tests/test_encryptor.py`.

## Example usage