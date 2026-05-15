import pytest

from api.data import memory_store
from api.services.alert_service import (
    AlertActionError,
    AlertNotFoundError,
    classify_alert,
    resolve_alert,
)


# Limites de referência usados em todos os testes
LIMITS = {"temp_max": 28.0, "humidity_min": 40.0}


@pytest.mark.parametrize(
    "test_id, temp,  hum,  sensor_ok, esperado",
    [
        ("TU-57", 23.0, 60.0, False, None),
        ("TU-58", 23.0, 60.0, True,  None),
        ("TU-59", 23.0, 35.0, False, None),
        ("TU-60", 23.0, 35.0, True,  "Aviso"),
        ("TU-61", 30.0, 60.0, False, None),
        ("TU-62", 30.0, 60.0, True,  "Aviso"),
        ("TU-63", 30.0, 35.0, False, None),
        ("TU-64", 30.0, 35.0, True,  "Crítico"),
    ],
)
def test_classify_alert(test_id, temp, hum, sensor_ok, esperado):
    """
    Cobertura de Condições Múltiplas + MC/DC sobre classify_alert (TU-57 a TU-64).
    Exercita todas as 8 combinações de (C1, C2, C3).
    """
    result = classify_alert(temp, hum, LIMITS, sensor_ok)
    assert result == esperado, (
        f"[{test_id}] C1={temp > LIMITS['temp_max']}, "
        f"C2={hum < LIMITS['humidity_min']}, C3={sensor_ok} "
        f"→ esperado '{esperado}', obtido '{result}'"
    )


# ---------------------------------------------------------------------------
# Fixtures para resolve_alert (TU-89 a TU-100)
# ---------------------------------------------------------------------------

@pytest.fixture()
def alerta_pendente():
    memory_store.reset_alerts()
    alert = memory_store.add_alert(
        {"batch_id": 1, "level": "Aviso", "temp": 30.0, "humidity": 35.0}
    )
    yield alert
    memory_store.reset_alerts()


@pytest.fixture()
def alerta_resolvido():
    memory_store.reset_alerts()
    alert = memory_store.add_alert(
        {"batch_id": 1, "level": "Aviso", "temp": 30.0, "humidity": 35.0}
    )
    memory_store.update_alert(alert["id"], {"state": "resolvido"})
    yield alert
    memory_store.reset_alerts()


# ---------------------------------------------------------------------------
# TU-89 a TU-93 — PE: ação (resolvido / ignorado / inválida)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, action, justification, esperado",
    [
        ("TU-89", "resolvido", None,       "ok"),
        ("TU-90", "resolvido", "J" * 50,   "ok"),
        ("TU-91", "ignorado",  "J" * 50,   "ok"),
        ("TU-92", "ignorado",  None,        "erro"),
        ("TU-93", "cancelado", None,        "erro"),
    ],
)
def test_resolve_alert_acao(test_id, action, justification, esperado, alerta_pendente):
    """PE: resolve_alert — classes de ação válidas e inválidas (TU-89 a TU-93)."""
    if esperado == "erro":
        with pytest.raises(AlertActionError):
            resolve_alert(alerta_pendente["id"], action, justification)
    else:
        result = resolve_alert(alerta_pendente["id"], action, justification)
        assert result["state"] == action, (
            f"[{test_id}] esperado state='{action}', obtido '{result['state']}'"
        )


# ---------------------------------------------------------------------------
# TU-94 a TU-98 — VL: comprimento da justificação [10, 500] chars
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, length, esperado",
    [
        ("TU-94",   9, "erro"),
        ("TU-95",  10, "ok"),
        ("TU-96", 250, "ok"),
        ("TU-97", 500, "ok"),
        ("TU-98", 501, "erro"),
    ],
)
def test_resolve_alert_justificacao_vl(test_id, length, esperado, alerta_pendente):
    """VL: comprimento da justificação para 'ignorado' no intervalo [10, 500] (TU-94 a TU-98)."""
    justification = "A" * length
    if esperado == "erro":
        with pytest.raises(AlertActionError):
            resolve_alert(alerta_pendente["id"], "ignorado", justification)
    else:
        result = resolve_alert(alerta_pendente["id"], "ignorado", justification)
        assert result["state"] == "ignorado", (
            f"[{test_id}] length={length} → esperado state='ignorado', obtido '{result['state']}'"
        )


# ---------------------------------------------------------------------------
# TU-99 — PE: alerta não encontrado → AlertNotFoundError
# ---------------------------------------------------------------------------

def test_resolve_alert_nao_encontrado():
    """PE: resolve_alert com id inexistente lança AlertNotFoundError (TU-99)."""
    memory_store.reset_alerts()
    with pytest.raises(AlertNotFoundError):
        resolve_alert(9999, "resolvido")
    memory_store.reset_alerts()


# ---------------------------------------------------------------------------
# TU-100 — PE: alerta já resolvido → AlertActionError
# ---------------------------------------------------------------------------

def test_resolve_alert_ja_resolvido(alerta_resolvido):
    """PE: resolve_alert num alerta que não está 'pendente' lança AlertActionError (TU-100)."""
    with pytest.raises(AlertActionError):
        resolve_alert(alerta_resolvido["id"], "resolvido")
