import pytest


# ---------------------------------------------------------------------------
# TI-29 a TI-34 — POST /tasks e GET /tasks
# ---------------------------------------------------------------------------

def test_post_tasks_sem_token(client):
    """TI-29: POST /tasks sem token devolve 401."""
    r = client.post("/tasks", json={"batch_id": 1, "task_type": "rega"})
    assert r.status_code == 401


def test_post_tasks_tipo_valido(client, admin_h):
    """TI-30: POST /tasks com tipo válido devolve 201."""
    r = client.post("/tasks",
                    json={"batch_id": 1, "task_type": "rega"},
                    headers=admin_h)
    assert r.status_code == 201


def test_post_tasks_tipo_invalido(client, admin_h):
    """TI-31: POST /tasks com tipo inválido devolve 400."""
    r = client.post("/tasks",
                    json={"batch_id": 1, "task_type": "voar"},
                    headers=admin_h)
    assert r.status_code == 400


def test_post_tasks_sem_batch_id(client, admin_h):
    """TI-32: POST /tasks sem batch_id devolve 422 (validação Pydantic)."""
    r = client.post("/tasks", json={"task_type": "rega"}, headers=admin_h)
    assert r.status_code == 422


def test_get_tasks_com_token(client, admin_h):
    """TI-33: GET /tasks com token válido devolve 200."""
    r = client.get("/tasks", headers=admin_h)
    assert r.status_code == 200


def test_delete_tasks_metodo_errado(client, admin_h):
    """TI-34: DELETE /tasks devolve 405."""
    r = client.delete("/tasks", headers=admin_h)
    assert r.status_code == 405


def test_post_tasks_schema_resposta_completo(client, admin_h):
    """TI-68: POST /tasks devolve JSON com todos os campos do TaskResponse."""
    r = client.post("/tasks",
                    json={"batch_id": 1, "task_type": "rega", "scheduled_date": "2026-05-22"},
                    headers=admin_h)
    assert r.status_code == 201
    body = r.json()
    for field in ("id", "batch_id", "task_type", "scheduled_date"):
        assert field in body
    assert body["batch_id"] == 1
    assert body["task_type"] == "rega"
    assert body["scheduled_date"] == "2026-05-22"


def test_post_tasks_data_invalida(client, admin_h):
    """TI-78: POST /tasks com scheduled_date em formato inválido devolve 400."""
    r = client.post("/tasks",
                    json={"batch_id": 1, "task_type": "rega", "scheduled_date": "22-05-2026"},
                    headers=admin_h)
    assert r.status_code == 400
