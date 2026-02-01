import unittest
from app import app
from db import db

class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client
        self.db = db

    def tearDown(self):
        with self.app.app_context():
            self.db.session.remove()
            self.db.drop_all()

    def test_user_registration(self):
        response = self.client().post('/register',
                                      data={'name': 'test'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('User created successfully.', response.get_data(as_text=True))