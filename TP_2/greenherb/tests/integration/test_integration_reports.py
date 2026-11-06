import pytest


# ---------------------------------------------------------------------------
# TI-57 a TI-60 — GET /reports
# ---------------------------------------------------------------------------

def test_get_reports_sem_token(client):
    """TI-57: GET /reports sem token devolve 401."""
    r = client.get("/reports")
    assert r.status_code == 401


def test_get_reports_format_csv(client, admin_h):
    """TI-58: GET /reports?format=CSV com token devolve 200."""
    r = client.get("/reports?format=CSV", headers=admin_h)
    assert r.status_code == 200


def test_get_reports_format_excel(client, admin_h):
    """TI-59: GET /reports?format=Excel com token devolve 200."""
    r = client.get("/reports?format=Excel", headers=admin_h)
    assert r.status_code == 200


def test_get_reports_format_invalido(client, admin_h):
    """TI-60: GET /reports?format=PDF com token devolve 400."""
    r = client.get("/reports?format=PDF", headers=admin_h)
    assert r.status_code == 400


def test_post_reports_metodo_errado(client, admin_h):
    """TI-71: POST /reports devolve 405."""
    r = client.post("/reports", json={}, headers=admin_h)
    assert r.status_code == 405
