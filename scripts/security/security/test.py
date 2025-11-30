import pytest
import main
from flask_jwt_extended import decode_token

@pytest.fixture
def client():
    main.app.config['TESTING'] = True
    with main.app.test_client() as client:
        with main.app.app_context():
            main.db.create_all()
        yield client
        main.db.drop_all()

def test_register(client):
    rv = client.post('/register', json={'username': 'test', 'password': 'password123'})
    assert b'registered successfully' in rv.data

def test_login(client):
    client.post('/register', json={'username': 'test', 'password': 'password123'})
    rv = client.post('/login', json={'username': 'test', 'password': 'password123'})
    assert b'login successful' in rv.data
    assert 'token' in rv.get_json()

def test_user(client):
    client.post('/register', json={'username': 'test', 'password': 'password123'})
    rv = client.post('/login', json={'username': 'test', 'password': 'password123'})
    token = rv.get_json()['token']
    rv = client.get('/user', headers={'Authorization': f'Bearer {token}'})
    assert b'test' in rv.data

def test_invalid_login(client):
    rv = client.post('/login', json={'username': 'test', 'password': 'password123'})
    assert b'invalid username or password' in rv.data