# Password Strength Checker

This project is a password strength checker that uses regular expressions to evaluate the strength of a password.

# How it works

The function checks for the following password characteristics:
- At least 8 characters
- Contains both uppercase and lowercase characters
- Contains at least one digit
- Contains at least one special character

# How to run

1. Ensure you have Python 3.6+ installed on your machine.
2. Clone the repository to your local machine.
3. Navigate to the `security` directory.
4. Run `python3 password_checker.py` to execute the script.

# Example Usage

Run `python3 password_checker.py`

You will be prompted to enter a password. After entering a password, the script will evaluate the strength of the password and display the result.

# Notes on Architecture & Tradeoffs

The password strength checker uses regular expressions to evaluate the strength of a password, which is a simple and effective approach. However, it may not cover all possible password combinations and can be adjusted based on the password policy of specific applications.