import os
import unittest
import automation

class TestAutomation(unittest.TestCase):
    def setUp(self):
        self.url = "https://example.com/test.zip"
        self.directory = "test_dir"
        self.filename = "test.zip"

    def test_download_and_extract(self):
        automation.download_and_extract(self.url, self.directory)
        self.assertTrue(os.path.exists(os.path.join(self.directory, self.filename)))

    def tearDown(self):
        os.remove(os.path.join(self.directory, self.filename))
        os.rmdir(self.directory)

if __name__ == "__main__":
    unittest.main()