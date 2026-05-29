import pytest
from fastapi.testclient import TestClient

from api.data import memory_store
from api.main import api


@pytest.fixture(scope="function")
def client():
    with TestClient(api) as c:
        yield c


@pytest.fixture(autouse=True)
def estado_limpo():
    """Cada fluxo de sistema parte de um estado conhecido: domínio vazio,
    apenas os utilizadores predefinidos (seed mínimo)."""
    memory_store.reset_herbs()
    memory_store.reset_plans()
    memory_store.reset_batches()
    memory_store.reset_alerts()
    memory_store.reset_measurements()
    yield
    memory_store.reset_herbs()
    memory_store.reset_plans()
    memory_store.reset_batches()
    memory_store.reset_alerts()
    memory_store.reset_measurements()


def _login(client, username, password):
    r = client.post("/auth/login", json={"username": username, "password": password})
    assert r.status_code == 200, f"login falhou: {r.text}"
    return r.json()["access_token"]


@pytest.fixture()
def admin_token(client):
    return _login(client, "admin", "admin123")


@pytest.fixture()
def resp_token(client):
    return _login(client, "responsavel", "responsavel123")
