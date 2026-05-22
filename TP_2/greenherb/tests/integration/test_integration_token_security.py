from datetime import datetime, timedelta, timezone
from uuid import uuid4

import jwt
import pytest

from api.data import memory_store
from api.services.auth_service import ALGORITHM, SECRET_KEY, generate_token


# ---------------------------------------------------------------------------
# Helpers para gerar tokens "atacados"
# ---------------------------------------------------------------------------

def _admin_user():
    return memory_store.public_user(memory_store.find_user_by_username("admin"))


def _expired_access_token() -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": "admin", "id": 3, "username": "admin", "user_id": 3,
        "role": "Administrador", "type": "access",
        "iat": now - timedelta(hours=2),
        "exp": now - timedelta(hours=1),         # expirou há 1 hora
        "jti": str(uuid4()),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def _tampered_access_token() -> str:
    token = generate_token(_admin_user(), token_type="access")
    # altera os últimos 5 caracteres da assinatura
    return token[:-5] + "AAAAA"


# ---------------------------------------------------------------------------
# TI-81 a TI-84 — Segurança do JWT na camada HTTP
# ---------------------------------------------------------------------------

def test_token_expirado_devolve_401(client):
    """TI-81: pedido com access token expirado devolve 401."""
    headers = {"Authorization": f"Bearer {_expired_access_token()}"}
    r = client.get("/plans", headers=headers)
    assert r.status_code == 401


def test_token_vazio_devolve_401(client):
    """TI-82: pedido com Authorization vazio (apenas 'Bearer ') devolve 401."""
    r = client.get("/plans", headers={"Authorization": "Bearer "})
    assert r.status_code == 401


def test_token_adulterado_devolve_401(client):
    """TI-83: pedido com access token com assinatura alterada devolve 401."""
    headers = {"Authorization": f"Bearer {_tampered_access_token()}"}
    r = client.get("/plans", headers=headers)
    assert r.status_code == 401


def test_access_token_no_endpoint_refresh_devolve_401(client):
    """TI-84: passar um access token a /auth/refresh devolve 401 (esperado refresh)."""
    access = generate_token(_admin_user(), token_type="access")
    r = client.post("/auth/refresh", json={"refresh_token": access})
    assert r.status_code == 401


def test_token_valido_devolve_200(client):
    """TI-85: pedido autenticado com token válido (acesso, não expirado, assinatura ok) devolve 200."""
    access = generate_token(_admin_user(), token_type="access")
    r = client.get("/plans", headers={"Authorization": f"Bearer {access}"})
    assert r.status_code == 200
    assert "plans" in r.json()
