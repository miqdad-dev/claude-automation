# Encryption-Decryption Microservice

This is a simple Flask app that provides two endpoints to encrypt and decrypt data using symmetric encryption.

## How it works

It uses the cryptography library's Fernet symmetric encryption to encrypt the data. When you send a POST request with some data to the `/encrypt` endpoint, it generates a new key, encrypts the data using that key, and returns both the key and the encrypted data. You can then send the key and the encrypted data to the `/decrypt` endpoint to decrypt the data.

## How to run

1. Install the requirements: