import re

def password_strength(password):
    if len(password) < 8:
        return 'Password must be at least 8 characters long'
    elif not re.search('[a-z]', password):
        return 'Password must contain at least one lowercase letter'
    elif not re.search('[A-Z]', password):
        return 'Password must contain at least one uppercase letter'
    elif not re.search('[0-9]', password):
        return 'Password must contain at least one digit'
    elif not re.search('[@_!#$%^&*()<>?/\\|}{~:]', password):
        return 'Password must contain at least one special character'
    else:
        return 'Password is strong'

def main():
    password = input("Enter your password: ")
    print(password_strength(password))

if __name__ == "__main__":
    main()