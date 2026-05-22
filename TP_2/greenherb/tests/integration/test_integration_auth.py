import pytest


# ---------------------------------------------------------------------------
# TI-01 a TI-07 — POST /auth/login e POST /auth/refresh
# ---------------------------------------------------------------------------

def test_login_credenciais_validas(client):
    """TI-01: credenciais válidas devolvem 200 com access_token e refresh_token."""
    r = client.post("/auth/login", json={"username": "admin", "password": "admin123"})
    assert r.status_code == 200
    body = r.json()
    assert "access_token" in body
    assert "refresh_token" in body


def test_login_password_errada(client):
    """TI-02: password errada devolve 401."""
    r = client.post("/auth/login", json={"username": "admin", "password": "errada"})
    assert r.status_code == 401


def test_login_username_inexistente(client):
    """TI-03: username inexistente devolve 401."""
    r = client.post("/auth/login", json={"username": "fantasma", "password": "x"})
    assert r.status_code == 401


def test_login_payload_vazio(client):
    """TI-04: payload vazio devolve 400 ou 422."""
    r = client.post("/auth/login", json={})
    assert r.status_code in (400, 422)


def test_refresh_token_valido(client):
    """TI-05: refresh token válido devolve 200 com novo par de tokens."""
    login = client.post("/auth/login", json={"username": "admin", "password": "admin123"})
    refresh_tok = login.json()["refresh_token"]
    r = client.post("/auth/refresh", json={"refresh_token": refresh_tok})
    assert r.status_code == 200
    assert "access_token" in r.json()


def test_refresh_token_malformado(client):
    """TI-06: refresh token malformado devolve 401."""
    r = client.post("/auth/refresh", json={"refresh_token": "token-invalido"})
    assert r.status_code == 401


def test_get_login_metodo_errado(client):
    """TI-07: GET /auth/login devolve 405 (método não permitido)."""
    r = client.get("/auth/login")
    assert r.status_code == 405
