import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_index(client):
    r = client.get('/')
    assert r.status_code == 200
    assert b'Hello' in r.data

def test_health(client):
    r = client.get('/health')
    assert r.status_code == 200
    assert b'ok' in r.data
