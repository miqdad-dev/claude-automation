import requests

def test_website():
    response = requests.get('http://localhost:8080')

    assert response.status_code == 200
    assert 'Welcome to my website!' in response.text