import pytest

from api.data import memory_store
from api.services.measurement_service import MeasurementValidationError, create_measurement


_BATCH_SEED = [
    {
        "id": 1, "herb_id": 1, "plan_id": None,
        "state": "ativo", "planned_qty": 100.0,
        "actual_qty": None, "losses": None, "productivity": None,
    }
]


@pytest.fixture()
def store_medicoes():
    memory_store.reset_batches(seed=_BATCH_SEED)
    memory_store.reset_measurements()
    memory_store.reset_alerts()
    yield
    memory_store.reset_batches()
    memory_store.reset_measurements()
    memory_store.reset_alerts()


# ---------------------------------------------------------------------------
# TU-101 a TU-104 — PE: campos obrigatórios em falta → MeasurementValidationError
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, payload, campo_em_falta",
    [
        ("TU-101", {"temp": 23.0, "humidity": 60.0, "luminosity": 15000}, "batch_id"),
        ("TU-102", {"batch_id": 1, "humidity": 60.0, "luminosity": 15000}, "temp"),
        ("TU-103", {"batch_id": 1, "temp": 23.0, "luminosity": 15000},    "humidity"),
        ("TU-104", {"batch_id": 1, "temp": 23.0, "humidity": 60.0},       "luminosity"),
    ],
)
def test_create_measurement_campo_obrigatorio(test_id, payload, campo_em_falta):
    """PE: campo obrigatório ausente lança MeasurementValidationError (TU-101 a TU-104)."""
    with pytest.raises(MeasurementValidationError):
        create_measurement(payload)


# ---------------------------------------------------------------------------
# TU-105 — PE: medição válida dentro dos limites → sem alerta gerado
# ---------------------------------------------------------------------------

def test_create_measurement_valida_sem_alerta(store_medicoes):
    """PE: medição com todos os campos válidos e leituras dentro dos limites → alerta=None (TU-105)."""
    payload = {
        "batch_id": 1,
        "temp": 23.0,
        "humidity": 60.0,
        "luminosity": 15000,
        "sensor_ok": True,
    }
    result = create_measurement(payload)

    assert result["batch_id"] == 1
    assert result["temp"] == 23.0
    assert result["alert"] is None


# ---------------------------------------------------------------------------
# TU-106 — PE: medição com temperatura acima do limite → alerta gerado automaticamente
# ---------------------------------------------------------------------------

def test_create_measurement_gera_alerta(store_medicoes):
    """PE: medição com temp > 28 e sensor_ok=True gera alerta automático (TU-106)."""
    payload = {
        "batch_id": 1,
        "temp": 30.0,
        "humidity": 60.0,
        "luminosity": 15000,
        "sensor_ok": True,
    }
    result = create_measurement(payload)

    assert result["alert"] is not None
    assert result["alert"]["level"] == "Aviso"
    assert result["alert"]["batch_id"] == 1
