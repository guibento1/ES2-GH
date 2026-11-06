import pytest


# ---------------------------------------------------------------------------
# TI-21 a TI-28 — POST /batches, PATCH /batches/{id}/close, GET /batches
# ---------------------------------------------------------------------------

def test_post_batches_sem_token(client):
    """TI-21: POST /batches sem token devolve 401."""
    r = client.post("/batches", json={"herb_id": 1, "planned_qty": 100.0})
    assert r.status_code == 401


def test_post_batches_payload_valido(client, admin_h):
    """TI-22: POST /batches com payload válido devolve 201."""
    r = client.post("/batches", json={"herb_id": 1, "planned_qty": 50.0}, headers=admin_h)
    assert r.status_code == 201
    assert r.json()["state"] == "ativo"


def test_post_batches_sem_herb_id(client, admin_h):
    """TI-23: POST /batches sem herb_id devolve 422 (validação de schema)."""
    r = client.post("/batches", json={"planned_qty": 100.0}, headers=admin_h)
    assert r.status_code == 422


def test_post_batches_planned_qty_zero(client, admin_h):
    """TI-24: POST /batches com planned_qty=0 devolve 400."""
    r = client.post("/batches", json={"herb_id": 1, "planned_qty": 0}, headers=admin_h)
    assert r.status_code == 400


def test_close_batch_ativo(client, admin_h):
    """TI-25: PATCH /batches/1/close num lote ativo devolve 200 com state concluído."""
    r = client.patch("/batches/1/close",
                     json={"has_losses": False, "actual_qty": 90.0, "losses": 0.0},
                     headers=admin_h)
    assert r.status_code == 200
    assert r.json()["state"] == "concluído"


def test_close_batch_ja_concluido(client, admin_h):
    """TI-26: PATCH /batches/1/close num lote já concluído devolve 400."""
    client.patch("/batches/1/close",
                 json={"has_losses": False, "actual_qty": 90.0, "losses": 0.0},
                 headers=admin_h)
    r = client.patch("/batches/1/close",
                     json={"has_losses": False, "actual_qty": 90.0, "losses": 0.0},
                     headers=admin_h)
    assert r.status_code == 400


def test_close_batch_id_inexistente(client, admin_h):
    """TI-27: PATCH /batches/9999/close com id inexistente devolve 404."""
    r = client.patch("/batches/9999/close",
                     json={"has_losses": False, "actual_qty": 90.0, "losses": 0.0},
                     headers=admin_h)
    assert r.status_code == 404


def test_get_batches_com_token(client, admin_h):
    """TI-28: GET /batches com token válido devolve 200."""
    r = client.get("/batches", headers=admin_h)
    assert r.status_code == 200
    assert "batches" in r.json()


def test_post_batches_schema_resposta_completo(client, admin_h):
    """TI-67: POST /batches devolve JSON com todos os campos do BatchResponse."""
    r = client.post("/batches",
                    json={"herb_id": 1, "plan_id": None, "planned_qty": 50.0},
                    headers=admin_h)
    assert r.status_code == 201
    body = r.json()
    for field in ("id", "herb_id", "plan_id", "state", "planned_qty",
                  "actual_qty", "losses", "productivity"):
        assert field in body
    assert body["herb_id"] == 1
    assert body["state"] == "ativo"
    assert body["planned_qty"] == 50.0


def test_post_batches_tipo_errado(client, admin_h):
    """TI-75: POST /batches com herb_id como string devolve 422 (tipo errado Pydantic)."""
    r = client.post("/batches",
                    json={"herb_id": "abc", "planned_qty": 50.0},
                    headers=admin_h)
    assert r.status_code == 422
