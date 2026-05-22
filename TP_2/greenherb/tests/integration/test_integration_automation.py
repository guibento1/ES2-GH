import pytest


# ---------------------------------------------------------------------------
# TI-49 a TI-52 — POST /automation/evaluate
# ---------------------------------------------------------------------------

def test_automation_sem_token(client):
    """TI-49: POST /automation/evaluate sem token devolve 401."""
    r = client.post("/automation/evaluate",
                    json={"mode": "Automático", "rule_active": True, "measurement_recent": True})
    assert r.status_code == 401


def test_automation_modo_automatico_executada(client, admin_h):
    """TI-50: modo Automático + regra ativa + medição recente devolve 200 com decision='executada'."""
    r = client.post("/automation/evaluate",
                    json={"mode": "Automático", "rule_active": True, "measurement_recent": True},
                    headers=admin_h)
    assert r.status_code == 200
    assert r.json()["decision"] == "executada"


def test_automation_modo_manual_sugerida(client, admin_h):
    """TI-51: modo Manual + regra ativa + medição recente devolve 200 com decision='sugerida'."""
    r = client.post("/automation/evaluate",
                    json={"mode": "Manual", "rule_active": True, "measurement_recent": True},
                    headers=admin_h)
    assert r.status_code == 200
    assert r.json()["decision"] == "sugerida"


def test_automation_regra_inativa_ignorada(client, admin_h):
    """TI-52: regra inativa devolve 200 com decision='ignorada'."""
    r = client.post("/automation/evaluate",
                    json={"mode": "Automático", "rule_active": False, "measurement_recent": True},
                    headers=admin_h)
    assert r.status_code == 200
    assert r.json()["decision"] == "ignorada"
