import pytest
from fastapi.testclient import TestClient
from app.main import app
from app import db
import asyncio

client = TestClient(app)


@pytest.fixture(scope="module", autouse=True)
def setup_db():
    """Inicializa y cierra el pool de DB para las pruebas."""
    loop = asyncio.get_event_loop()
    loop.run_until_complete(db.init_db_pool())
    yield
    loop.run_until_complete(db.close_db_pool())


def test_login_correct_credentials():
    """Debe retornar 200 si las credenciales son correctas."""
    response = client.post("/api/login", json={
        "email": "admin@example.com",
        "password": "admin"
    })
    assert response.status_code == 200
    assert response.json().get("message") == "ok"


def test_login_incorrect_credentials():
    """Debe retornar 401 si las credenciales son incorrectas."""
    response = client.post("/api/login", json={
        "email": "admin@example.com",
        "password": "wrongpass"
    })
    assert response.status_code == 401
