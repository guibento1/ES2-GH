import pytest

from api.data import memory_store


@pytest.fixture()
def alert_id():
    alert = memory_store.add_alert(
        {"batch_id": 1, "level": "Aviso", "temp": 30.0, "humidity": 35.0}
    )
    return alert["id"]


# ---------------------------------------------------------------------------
# TI-41 a TI-48 — PATCH /alerts/{id} e GET /alerts
# ---------------------------------------------------------------------------

def test_patch_alerts_sem_token(client, alert_id):
    """TI-41: PATCH /alerts/{id} sem token devolve 401."""
    r = client.patch(f"/alerts/{alert_id}", json={"action": "resolvido"})
    assert r.status_code == 401


def test_get_alerts_com_token(client, admin_h):
    """TI-42: GET /alerts com token devolve 200."""
    r = client.get("/alerts", headers=admin_h)
    assert r.status_code == 200
    assert "alerts" in r.json()


def test_patch_alert_resolvido_sem_justificacao(client, admin_h, alert_id):
    """TI-43: PATCH /alerts/{id} resolvido sem justificação devolve 200."""
    r = client.patch(f"/alerts/{alert_id}",
                     json={"action": "resolvido"},
                     headers=admin_h)
    assert r.status_code == 200
    assert r.json()["state"] == "resolvido"


def test_patch_alert_ignorado_justificacao_valida(client, admin_h, alert_id):
    """TI-44: PATCH /alerts/{id} ignorado com justificação válida devolve 200."""
    r = client.patch(f"/alerts/{alert_id}",
                     json={"action": "ignorado", "justification": "J" * 50},
                     headers=admin_h)
    assert r.status_code == 200
    assert r.json()["state"] == "ignorado"


def test_patch_alert_ignorado_sem_justificacao(client, admin_h, alert_id):
    """TI-45: PATCH /alerts/{id} ignorado sem justificação devolve 422."""
    r = client.patch(f"/alerts/{alert_id}",
                     json={"action": "ignorado"},
                     headers=admin_h)
    assert r.status_code == 422


def test_patch_alert_justificacao_9_chars(client, admin_h, alert_id):
    """TI-46: PATCH /alerts/{id} ignorado com justificação de 9 chars devolve 422 (VL abaixo do mínimo)."""
    r = client.patch(f"/alerts/{alert_id}",
                     json={"action": "ignorado", "justification": "A" * 9},
                     headers=admin_h)
    assert r.status_code == 422


def test_patch_alert_justificacao_501_chars(client, admin_h, alert_id):
    """TI-47: PATCH /alerts/{id} ignorado com justificação de 501 chars devolve 422 (VL acima do máximo)."""
    r = client.patch(f"/alerts/{alert_id}",
                     json={"action": "ignorado", "justification": "A" * 501},
                     headers=admin_h)
    assert r.status_code == 422


def test_patch_alert_id_inexistente(client, admin_h):
    """TI-48: PATCH /alerts/9999 com id inexistente devolve 404."""
    r = client.patch("/alerts/9999",
                     json={"action": "resolvido"},
                     headers=admin_h)
    assert r.status_code == 404
