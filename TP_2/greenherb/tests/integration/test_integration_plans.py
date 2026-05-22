import pytest


# ---------------------------------------------------------------------------
# TI-14 a TI-20 — POST /plans e GET /plans
# ---------------------------------------------------------------------------

def test_post_plans_sem_token(client):
    """TI-14: POST /plans sem token devolve 401."""
    r = client.post("/plans", json={"type": "regular"})
    assert r.status_code == 401


def test_post_plans_tipo_regular(client, admin_h):
    """TI-15: POST /plans com tipo regular e token válido devolve 201."""
    r = client.post("/plans", json={"type": "regular"}, headers=admin_h)
    assert r.status_code == 201
    assert r.json()["type"] == "regular"


def test_post_plans_tipo_invalido(client, admin_h):
    """TI-16: POST /plans com tipo inválido devolve 400."""
    r = client.post("/plans", json={"type": "invalido"}, headers=admin_h)
    assert r.status_code == 400


def test_post_plans_pontual_sem_autorizacao(client, admin_h):
    """TI-17: POST /plans pontual sem authorized_by devolve 400."""
    r = client.post("/plans", json={"type": "pontual"}, headers=admin_h)
    assert r.status_code == 400


def test_post_plans_pontual_com_autorizacao(client, admin_h):
    """TI-18: POST /plans pontual com authorized_by devolve 201."""
    r = client.post("/plans",
                    json={"type": "pontual", "authorized_by": "responsavel"},
                    headers=admin_h)
    assert r.status_code == 201
    assert r.json()["authorized_by"] == "responsavel"


def test_get_plans_com_token(client, admin_h):
    """TI-19: GET /plans com token válido devolve 200 com lista de planos."""
    r = client.get("/plans", headers=admin_h)
    assert r.status_code == 200
    assert "plans" in r.json()


def test_delete_plans_metodo_errado(client, admin_h):
    """TI-20: DELETE /plans devolve 405 (método não permitido)."""
    r = client.delete("/plans", headers=admin_h)
    assert r.status_code == 405


def test_post_plans_token_malformado(client):
    """TI-65: POST /plans com token malformado devolve 401."""
    r = client.post("/plans",
                    json={"type": "regular"},
                    headers={"Authorization": "Bearer token-invalido"})
    assert r.status_code == 401


def test_post_plans_schema_resposta_completo(client, admin_h):
    """TI-66: POST /plans regular devolve JSON com todos os campos do PlanResponse."""
    payload = {
        "type": "regular",
        "temp_min": 20.0, "temp_max": 26.0,
        "humidity_min": 50.0, "humidity_max": 70.0,
        "luminosity_min": 8000, "luminosity_max": 20000,
        "duration_days": 90,
    }
    r = client.post("/plans", json=payload, headers=admin_h)
    assert r.status_code == 201
    body = r.json()
    for field in ("id", "type", "temp_min", "temp_max", "humidity_min",
                  "humidity_max", "luminosity_min", "luminosity_max", "duration_days"):
        assert field in body
    assert body["type"] == "regular"
    assert body["temp_min"] == 20.0
    assert body["duration_days"] == 90


def test_post_plans_tipo_errado(client, admin_h):
    """TI-74: POST /plans com temp_min como string devolve 422 (tipo errado Pydantic)."""
    r = client.post("/plans",
                    json={"type": "regular", "temp_min": "muito"},
                    headers=admin_h)
    assert r.status_code == 422
