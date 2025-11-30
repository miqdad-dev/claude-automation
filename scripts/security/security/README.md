# Basic Authentication System

This is a simple authentication system built in Python using the Flask framework and SQLite for the database. It uses bcrypt for password hashing.

### What it does
This system provides REST API endpoints for registration, login, and user detail retrieval. It's a basic implementation of secure user authentication.

### How it works
- `registration`: Users can register by providing a username and password. The password is hashed and both the username and hashed password are stored in the SQLite database.
- `login`: The user logs in with their username and password, and the system checks if the username exists and if the hashed password matches the stored hashed password. If successful, the user is logged in and a token is returned.
- `user detail retrieval`: A user can retrieve their details by passing in their token.

### How to run
1. Install Python 3.8 or later
2. Install the required packages with `pip install -r requirements.txt`
3. Run the program with `python main.py`

### Example usage
- Register a new user: `POST http://localhost:5000/register {"username": "test", "password": "password123"}`
- Log in: `POST http://localhost:5000/login {"username": "test", "password": "password123"}`
- Retrieve user details: `GET http://localhost:5000/user -H "Authorization: Bearer <token>"`

### Notes on architecture & tradeoffs
This is a simple implementation of an authentication system and does not include features like password resetting, two-factor authentication, or email verification. The SQLite database is used for simplicity, but for a production system, a more robust database system should be used.