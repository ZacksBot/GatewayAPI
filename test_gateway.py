import pytest
from gateway import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_csv_response(client):
    response = client.get('/vulnerabilities')
    assert response.status_code == 200
    assert response.mimetype == 'text/csv'

def test_json_response(client):
    response = client.get('/vulnerabilities?format=json')
    assert response.status_code == 200
    assert response.mimetype == 'application/json'
    data = response.get_json()
    assert "Items" in data
    assert isinstance(data["Items"], list)
