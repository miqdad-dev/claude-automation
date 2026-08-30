import os
import shutil
import unittest
from main import get_files_from_dir, categorize_files, move_files

class TestFileOrganizer(unittest.TestCase):

    def setUp(self):
        self.test_dir = '/tmp/test_dir'
        self.target_dir = '/tmp/target_dir'
        os.makedirs(self.test_dir, exist_ok=True)
        os.makedirs(self.target_dir, exist_ok=True)
        self.test_files = ['test1.txt', 'test2.py', 'test3.txt', 'test4.py', 'test5.md']
        for file in self.test_files:
            open(os.path.join(self.test_dir, file), 'a').close()

    def tearDown(self):
        shutil.rmtree(self.test_dir)
        shutil.rmtree(self.target_dir)

    def test_get_files_from_dir(self):
        files = get_files_from_dir(self.test_dir)
        self.assertEqual(set(files), set(self.test_files))

    def test_categorize_files(self):
        files = get_files_from_dir(self.test_dir)
        categorized_files = categorize_files(files, self.test_dir)
        self.assertEqual(set(categorized_files.keys()), set(['txt', 'py', 'md']))
        self.assertEqual(len(categorized_files['txt']), 2)
        self.assertEqual(len(categorized_files['py']), 2)
        self.assertEqual(len(categorized_files['md']), 1)

    def test_move_files(self):
        files = get_files_from_dir(self.test_dir)
        categorized_files = categorize_files(files, self.test_dir)
        move_files(categorized_files, self.target_dir)
        self.assertEqual(len(os.listdir(self.target_dir)), 3)
        self.assertEqual(len(os.listdir(os.path.join(self.target_dir, 'txt'))), 2)
        self.assertEqual(len(os.listdir(os.path.join(self.target_dir, 'py'))), 2)
        self.assertEqual(len(os.listdir(os.path.join(self.target_dir, 'md'))), 1)

if __name__ == '__main__':
    unittest.main()