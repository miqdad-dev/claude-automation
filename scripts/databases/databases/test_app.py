import pytest
import app

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        with app.app.app_context():
            app.db.create_all()
        yield client

def test_get_users(client):
    rv = client.get('/users')
    assert b'Alice' in rv.data
    assert b'Bob' in rv.data

def test_add_user(client):
    rv = client.post('/users', json={'name': 'John', 'email': 'john@example.com'})
    assert b'User added successfully' in rv.data
    rv = client.get('/users')
    assert b'John' in rv.data