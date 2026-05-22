import pytest


_PAYLOAD_NORMAL = {
    "batch_id": 1, "temp": 23.0, "humidity": 60.0,
    "luminosity": 15000, "sensor_ok": True,
}
_PAYLOAD_FORA = {
    "batch_id": 1, "temp": 30.0, "humidity": 60.0,
    "luminosity": 15000, "sensor_ok": True,
}
_PAYLOAD_SENSOR_OFF = {
    "batch_id": 1, "temp": 30.0, "humidity": 35.0,
    "luminosity": 1000, "sensor_ok": False,
}


# ---------------------------------------------------------------------------
# TI-35 a TI-40 — POST /measurements e GET /measurements
# ---------------------------------------------------------------------------

def test_post_measurements_sem_token(client):
    """TI-35: POST /measurements sem token devolve 401."""
    r = client.post("/measurements", json=_PAYLOAD_NORMAL)
    assert r.status_code == 401


def test_post_measurements_dentro_limites(client, admin_h):
    """TI-36: POST /measurements com leituras dentro dos limites devolve 201 sem alerta."""
    r = client.post("/measurements", json=_PAYLOAD_NORMAL, headers=admin_h)
    assert r.status_code == 201
    assert r.json()["alert"] is None


def test_post_measurements_fora_limites(client, admin_h):
    """TI-37: POST /measurements com temp fora dos limites devolve 201 com alerta Aviso."""
    r = client.post("/measurements", json=_PAYLOAD_FORA, headers=admin_h)
    assert r.status_code == 201
    body = r.json()
    assert body["alert"] is not None
    assert body["alert"]["level"] == "Aviso"


def test_post_measurements_sensor_off(client, admin_h):
    """TI-38: POST /measurements com sensor_ok=False devolve 201 sem alerta."""
    r = client.post("/measurements", json=_PAYLOAD_SENSOR_OFF, headers=admin_h)
    assert r.status_code == 201
    assert r.json()["alert"] is None


def test_get_measurements_com_token(client, admin_h):
    """TI-39: GET /measurements com token devolve 200."""
    r = client.get("/measurements", headers=admin_h)
    assert r.status_code == 200


def test_post_measurements_campos_em_falta(client, admin_h):
    """TI-40: POST /measurements sem luminosity devolve 422 (schema) ou 400 (validação)."""
    r = client.post("/measurements",
                    json={"batch_id": 1, "temp": 23.0, "humidity": 60.0},
                    headers=admin_h)
    assert r.status_code in (400, 422)
