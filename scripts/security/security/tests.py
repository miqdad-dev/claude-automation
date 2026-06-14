import unittest
from password_checker import password_strength

class TestPasswordStrength(unittest.TestCase):

    def test_length(self):
        self.assertEqual(password_strength('abc'), 'Password must be at least 8 characters long')

    def test_lowercase(self):
        self.assertEqual(password_strength('ABCDEFGH'), 'Password must contain at least one lowercase letter')

    def test_uppercase(self):
        self.assertEqual(password_strength('abcdefgh'), 'Password must contain at least one uppercase letter')

    def test_digit(self):
        self.assertEqual(password_strength('Abcdefgh'), 'Password must contain at least one digit')

    def test_special_character(self):
        self.assertEqual(password_strength('Abcdefgh1'), 'Password must contain at least one special character')

    def test_strong_password(self):
        self.assertEqual(password_strength('Abcdefgh1!'), 'Password is strong')

if __name__ == '__main__':
    unittest.main()