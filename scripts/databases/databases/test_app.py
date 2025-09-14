import pytest
from app import app, db, User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.session.remove()
        db.drop_all()

def test_create_user(client):
    response = client.post('/users', json={'username': 'test'})
    assert response.status_code == 201
    assert response.get_json() == {'id': 1, 'username': 'test'}

def test_create_existing_user(client):
    client.post('/users', json={'username': 'test'})
    response = client.post('/users', json={'username': 'test'})
    assert response.status_code == 400

def test_get_user(client):
    client.post('/users', json={'username': 'test'})
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.get_json() == {'id': 1, 'username': 'test'}

def test_get_non_existent_user(client):
    response = client.get('/users/1')
    assert response.status_code == 404