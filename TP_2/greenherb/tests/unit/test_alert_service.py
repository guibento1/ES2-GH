import pytest

from api.data import memory_store
from api.services.alert_service import (
    AlertActionError,
    AlertNotFoundError,
    classify_alert,
    resolve_alert,
)

LIMITS = {
    "temp_min": 18.0, "temp_max": 28.0,
    "humidity_min": 40.0, "humidity_max": 80.0,
    "luminosity_min": 5000, "luminosity_max": 25000,
}

# ---------------------------------------------------------------------------
# Fixtures
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
# TU-108 a TU-115 — PE: classificação de alertas
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, temp, hum, lux, sensor_ok, esperado",
    [
        ("TU-108", 23.0, 60.0, 15000, True,  None),           # PE: tudo normal → sem alerta
        ("TU-109", 29.0, 60.0, 15000, True,  "Aviso"),        # PE: temperatura alta
        ("TU-110", 17.0, 60.0, 15000, True,  "Aviso"),        # PE: temperatura baixa
        ("TU-111", 23.0, 85.0, 15000, True,  "Aviso"),        # PE: humidade alta
        ("TU-112", 23.0, 35.0, 15000, True,  "Aviso"),        # PE: humidade baixa
        ("TU-113", 29.0, 35.0, 15000, True,  "Crítico"),      # PE: temp + hum ambas fora
        ("TU-114", 23.0, 60.0, 26000, True,  "Informativo"),  # PE: luminosidade fora
        ("TU-115", 29.0, 35.0, 26000, False, None),           # PE: sensor off → sem alerta
    ],
)
def test_classify_alert(test_id, temp, hum, lux, sensor_ok, esperado):
    """PE: classify_alert — classes None / Aviso / Crítico / Informativo (TU-108 a TU-115)."""
    assert classify_alert(temp, hum, lux, LIMITS, sensor_ok) == esperado


# ---------------------------------------------------------------------------
# TU-116 a TU-120 — PE: resolução de alerta — ação
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, action, justification, esperado",
    [
        ("TU-116", "resolvido", None,      "ok"),    # PE: resolvido sem justificação (opcional)
        ("TU-117", "resolvido", "J" * 50,  "ok"),    # PE: resolvido com justificação (aceite)
        ("TU-118", "ignorado",  "J" * 50,  "ok"),    # PE: ignorado com justificação válida
        ("TU-119", "ignorado",  None,      "erro"),  # PE: ignorado sem justificação obrigatória
        ("TU-120", "cancelado", None,      "erro"),  # PE: ação inválida
    ],
)
def test_resolve_alert_acao(test_id, action, justification, esperado, alerta_pendente):
    """PE: resolve_alert — classes de ação (TU-116 a TU-120)."""
    if esperado == "erro":
        with pytest.raises(AlertActionError):
            resolve_alert(alerta_pendente["id"], action, justification)
    else:
        result = resolve_alert(alerta_pendente["id"], action, justification)
        assert result["state"] == action


# ---------------------------------------------------------------------------
# TU-121 a TU-125 — VL: comprimento da justificação [10, 500] chars
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, length, esperado",
    [
        ("TU-121",   9, "erro"),   # VL: abaixo do limite inferior (9 < 10)
        ("TU-122",  10, "ok"),     # VL: limite inferior exacto
        ("TU-123", 250, "ok"),     # VL: valor nominal interior
        ("TU-124", 500, "ok"),     # VL: limite superior exacto
        ("TU-125", 501, "erro"),   # VL: acima do limite superior (501 > 500)
    ],
)
def test_resolve_alert_justificacao_vl(test_id, length, esperado, alerta_pendente):
    """VL: justificação para 'ignorado' no intervalo [10, 500] chars (TU-121 a TU-125)."""
    justification = "A" * length
    if esperado == "erro":
        with pytest.raises(AlertActionError):
            resolve_alert(alerta_pendente["id"], "ignorado", justification)
    else:
        result = resolve_alert(alerta_pendente["id"], "ignorado", justification)
        assert result["state"] == "ignorado"


# ---------------------------------------------------------------------------
# TU-126 — PE: alerta não encontrado
# ---------------------------------------------------------------------------

def test_resolve_alert_nao_encontrado():
    """PE: id inexistente lança AlertNotFoundError (TU-126)."""
    memory_store.reset_alerts()
    with pytest.raises(AlertNotFoundError):
        resolve_alert(9999, "resolvido")
    memory_store.reset_alerts()


# ---------------------------------------------------------------------------
# TU-127 — PE: alerta já resolvido
# ---------------------------------------------------------------------------

def test_resolve_alert_ja_resolvido(alerta_resolvido):
    """PE: alerta não pendente lança AlertActionError (TU-127)."""
    with pytest.raises(AlertActionError):
        resolve_alert(alerta_resolvido["id"], "resolvido")
