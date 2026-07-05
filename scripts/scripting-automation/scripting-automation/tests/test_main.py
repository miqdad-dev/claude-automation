import unittest
import os
import subprocess

class TestMain(unittest.TestCase):
    def test_main(self):
        directory = '.'
        extension = 'py'
        result = subprocess.run(['python', '../src/main.py', '-d', directory, '-e', extension],
                                stdout=subprocess.PIPE)
        self.assertIn('test_main.py', result.stdout.decode())

if __name__ == '__main__':
    unittest.main()