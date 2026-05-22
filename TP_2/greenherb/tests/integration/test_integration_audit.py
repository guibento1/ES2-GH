import pytest


# ---------------------------------------------------------------------------
# TI-61 a TI-64 — GET /audit
# ---------------------------------------------------------------------------

def test_get_audit_sem_token(client):
    """TI-61: GET /audit sem token devolve 401."""
    r = client.get("/audit")
    assert r.status_code == 401


def test_get_audit_tecnico_proibido(client, tech_h):
    """TI-62: GET /audit com perfil Técnico devolve 403."""
    r = client.get("/audit", headers=tech_h)
    assert r.status_code == 403


def test_get_audit_admin_aceite(client, admin_h):
    """TI-63: GET /audit com perfil Admin devolve 200."""
    r = client.get("/audit", headers=admin_h)
    assert r.status_code == 200


def test_post_audit_metodo_errado(client, admin_h):
    """TI-64: POST /audit devolve 405 (método não permitido)."""
    r = client.post("/audit", json={}, headers=admin_h)
    assert r.status_code == 405
