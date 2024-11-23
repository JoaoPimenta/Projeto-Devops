import json
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Testa a rota principal"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'API is running' in response.data

def test_get_items(client):
    """Testa a rota /items"""
    response = client.get('/items')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'items' in data
    assert len(data['items']) == 3

def test_login(client):
    """Testa o login e geração do token JWT"""
    response = client.post('/login')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'access_token' in data

def test_protected_without_token(client):
    """Testa a rota /protected sem o token"""
    response = client.get('/protected')
    assert response.status_code == 401
    assert b'Missing Authorization Header' in response.data

def test_protected_with_token(client):
    """Testa a rota /protected com o token JWT"""
    # Primeiro, faz login para obter o token
    login_response = client.post('/login')
    data = json.loads(login_response.data)
    token = data['access_token']

    # Agora, faz uma requisição para a rota protegida com o token
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = client.get('/protected', headers=headers)
    assert response.status_code == 200
    assert b'Protected route' in response.data
