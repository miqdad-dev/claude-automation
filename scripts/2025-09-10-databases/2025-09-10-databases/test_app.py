import json
import unittest
from app import app, db, User

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_creation(self):
        response = self.app.post('/user',
                                 data=json.dumps(dict(name='John Doe', email='john.doe@example.com')),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)
        user = User.query.filter_by(name='John Doe').first()
        self.assertIsNotNone(user)