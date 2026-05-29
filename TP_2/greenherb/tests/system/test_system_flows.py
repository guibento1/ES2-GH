"""Testes de sistema (end-to-end) sobre a API GREENHERB via TestClient.

Cada teste percorre um fluxo completo de negócio, encadeando vários endpoints
como um cliente real faria, validando o comportamento observável em cada passo.
"""


def _auth(token):
    return {"Authorization": f"Bearer {token}"}


# ---------------------------------------------------------------------------
# TS-01 — Ciclo completo de um lote
# Registar erva -> criar plano -> abrir lote -> tarefa -> medição -> fechar lote
# ---------------------------------------------------------------------------

def test_ts01_ciclo_completo_de_lote(client, admin_token):
    """TS-01: lote percorre ativo -> concluído com produtividade calculada."""
    h = _auth(admin_token)

    # 1. Registar a erva
    r = client.post("/herbs", json={"name": "Manjericão", "family": "Lamiaceae"}, headers=h)
    assert r.status_code == 201
    herb_id = r.json()["id"]

    # 2. Criar plano regular dentro dos limites
    r = client.post("/plans", json={
        "type": "regular", "temp_min": 18, "temp_max": 28,
        "humidity_min": 40, "humidity_max": 80,
        "luminosity_min": 5000, "luminosity_max": 25000, "duration_days": 90,
    }, headers=h)
    assert r.status_code == 201
    plan_id = r.json()["id"]

    # 3. Abrir o lote associado à erva e ao plano
    r = client.post("/batches", json={
        "herb_id": herb_id, "plan_id": plan_id, "planned_qty": 100.0,
    }, headers=h)
    assert r.status_code == 201
    batch = r.json()
    batch_id = batch["id"]
    assert batch["state"] == "ativo"

    # 4. Executar uma tarefa operacional
    r = client.post("/tasks", json={
        "batch_id": batch_id, "task_type": "rega", "scheduled_date": "2026-05-22",
    }, headers=h)
    assert r.status_code == 201

    # 5. Registar uma medição dentro dos limites (sem alerta)
    r = client.post("/measurements", json={
        "batch_id": batch_id, "temp": 23.0, "humidity": 60.0,
        "luminosity": 15000, "sensor_ok": True,
    }, headers=h)
    assert r.status_code == 201
    assert r.json()["alert"] is None

    # 6. Fechar o lote sem perdas e verificar produtividade
    r = client.patch(f"/batches/{batch_id}/close", json={
        "has_losses": False, "actual_qty": 100.0, "losses": 0.0,
    }, headers=h)
    assert r.status_code == 200
    fechado = r.json()
    assert fechado["state"] == "concluído"
    assert fechado["productivity"] == 100.0


# ---------------------------------------------------------------------------
# TS-02 — Gestão de incidente
# Medição fora dos limites gera alerta -> Responsável resolve o alerta
# ---------------------------------------------------------------------------

def test_ts02_gestao_de_incidente(client, admin_token, resp_token):
    """TS-02: medição crítica gera alerta que é depois resolvido com justificação."""
    ha = _auth(admin_token)

    # Preparar lote ativo
    r = client.post("/batches", json={"herb_id": 1, "planned_qty": 50.0}, headers=ha)
    batch_id = r.json()["id"]

    # 1. Medição com temperatura fora dos limites -> gera alerta
    r = client.post("/measurements", json={
        "batch_id": batch_id, "temp": 35.0, "humidity": 60.0,
        "luminosity": 15000, "sensor_ok": True,
    }, headers=ha)
    assert r.status_code == 201
    assert r.json()["alert"] is not None
    assert r.json()["alert"]["level"] == "Aviso"

    # 2. O alerta aparece na lista de alertas
    r = client.get("/alerts", headers=ha)
    assert r.status_code == 200
    alertas = r.json()["alerts"]
    assert len(alertas) >= 1
    alert_id = alertas[-1]["id"]

    # 3. Responsável resolve o alerta com justificação
    hr = _auth(resp_token)
    r = client.patch(f"/alerts/{alert_id}", json={
        "action": "resolvido", "justification": "Ventilação reforçada e temperatura normalizada.",
    }, headers=hr)
    assert r.status_code == 200
    assert r.json()["state"] == "resolvido"


# ---------------------------------------------------------------------------
# TS-03 — Controlo de acesso à auditoria
# Operações de leitura de auditoria respeitam o perfil do utilizador
# ---------------------------------------------------------------------------

def test_ts03_acesso_auditoria_por_perfil(client, admin_token):
    """TS-03: a auditoria só é acessível ao Administrador; outros perfis são barrados."""
    # Sem token -> 401
    r = client.get("/audit")
    assert r.status_code == 401

    # Técnico -> 403
    tec = _auth(client.post("/auth/login",
                            json={"username": "tecnico", "password": "tecnico123"}).json()["access_token"])
    r = client.get("/audit", headers=tec)
    assert r.status_code == 403

    # Administrador -> 200
    r = client.get("/audit", headers=_auth(admin_token))
    assert r.status_code == 200
