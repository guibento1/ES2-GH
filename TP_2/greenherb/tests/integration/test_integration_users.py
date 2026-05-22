import pytest


_USER_PAYLOAD = {
    "username": "novo_user",
    "password": "pass123",
    "full_name": "Novo Utilizador",
    "role": "Técnico",
}


# ---------------------------------------------------------------------------
# TI-53 a TI-56 — POST /users e GET /users
# ---------------------------------------------------------------------------

def test_post_users_sem_token(client):
    """TI-53: POST /users sem token devolve 401."""
    r = client.post("/users", json=_USER_PAYLOAD)
    assert r.status_code == 401


def test_post_users_tecnico_proibido(client, tech_h):
    """TI-54: POST /users com perfil Técnico devolve 403."""
    r = client.post("/users", json=_USER_PAYLOAD, headers=tech_h)
    assert r.status_code == 403


def test_post_users_admin_cria(client, admin_h):
    """TI-55: POST /users com perfil Admin devolve 201."""
    r = client.post("/users", json=_USER_PAYLOAD, headers=admin_h)
    assert r.status_code == 201
    body = r.json()
    assert body["username"] == "novo_user"
    assert body["role"] == "Técnico"


def test_get_users_com_token(client, admin_h):
    """TI-56: GET /users com token devolve 200."""
    r = client.get("/users", headers=admin_h)
    assert r.status_code == 200
    assert "users" in r.json()
