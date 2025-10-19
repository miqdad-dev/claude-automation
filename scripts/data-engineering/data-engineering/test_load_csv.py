import unittest
from load_csv import load_csv_to_db

class TestCsvLoader(unittest.TestCase):
    def test_load_csv_to_db(self):
        try:
            load_csv_to_db('test.csv', 'test')
            self.assertTrue(True)
        except:
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()