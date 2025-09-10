import app
import unittest
import json

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def tearDown(self):
        pass

    def test_compile(self):
        response = self.app.post('/compile', data=json.dumps({'code': 'print("Hello, world!")'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'output': 'Hello, world!\n'})

if __name__ == '__main__':
    unittest.main()