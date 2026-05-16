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
# TU-90 a TU-94 — VL: temperatura [18, 28] °C
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, temp, alerta_esperado",
    [
        ("TU-90", 17, True),   # VL: abaixo do limite inferior (17 < 18) → alerta
        ("TU-91", 18, False),  # VL: limite inferior exacto → sem alerta
        ("TU-92", 23, False),  # VL: valor nominal interior → sem alerta
        ("TU-93", 28, False),  # VL: limite superior exacto → sem alerta
        ("TU-94", 29, True),   # VL: acima do limite superior (29 > 28) → alerta
    ],
)
def test_measurement_temperatura_vl(test_id, temp, alerta_esperado, store_medicoes):
    """VL: temperatura [18, 28] °C — alerta gerado fora dos limites (TU-90 a TU-94)."""
    result = create_measurement({"batch_id": 1, "temp": temp, "humidity": 60.0,
                                 "luminosity": 15000, "sensor_ok": True})
    assert (result["alert"] is not None) == alerta_esperado


# ---------------------------------------------------------------------------
# TU-95 a TU-99 — VL: humidade [40, 80] %
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, hum, alerta_esperado",
    [
        ("TU-95", 39, True),   # VL: abaixo do limite inferior (39 < 40) → alerta
        ("TU-96", 40, False),  # VL: limite inferior exacto → sem alerta
        ("TU-97", 60, False),  # VL: valor nominal interior → sem alerta
        ("TU-98", 80, False),  # VL: limite superior exacto → sem alerta
        ("TU-99", 81, True),   # VL: acima do limite superior (81 > 80) → alerta
    ],
)
def test_measurement_humidade_vl(test_id, hum, alerta_esperado, store_medicoes):
    """VL: humidade [40, 80] % — alerta gerado fora dos limites (TU-95 a TU-99)."""
    result = create_measurement({"batch_id": 1, "temp": 23.0, "humidity": hum,
                                 "luminosity": 15000, "sensor_ok": True})
    assert (result["alert"] is not None) == alerta_esperado


# ---------------------------------------------------------------------------
# TU-100 a TU-104 — VL: luminosidade [5000, 25000] lux
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, lux, alerta_esperado",
    [
        ("TU-100",  4999, True),   # VL: abaixo do limite inferior (4999 < 5000) → alerta
        ("TU-101",  5000, False),  # VL: limite inferior exacto → sem alerta
        ("TU-102", 15000, False),  # VL: valor nominal interior → sem alerta
        ("TU-103", 25000, False),  # VL: limite superior exacto → sem alerta
        ("TU-104", 25001, True),   # VL: acima do limite superior (25001 > 25000) → alerta
    ],
)
def test_measurement_luminosidade_vl(test_id, lux, alerta_esperado, store_medicoes):
    """VL: luminosidade [5000, 25000] lux — alerta gerado fora dos limites (TU-100 a TU-104)."""
    result = create_measurement({"batch_id": 1, "temp": 23.0, "humidity": 60.0,
                                 "luminosity": lux, "sensor_ok": True})
    assert (result["alert"] is not None) == alerta_esperado


# ---------------------------------------------------------------------------
# TU-105 a TU-106 — PE: sensor_ok
# ---------------------------------------------------------------------------

def test_measurement_sensor_off_sem_alerta(store_medicoes):
    """PE: sensor_ok=False → sem alerta mesmo com leituras fora dos limites (TU-105)."""
    result = create_measurement({"batch_id": 1, "temp": 35.0, "humidity": 20.0,
                                 "luminosity": 1000, "sensor_ok": False})
    assert result["alert"] is None


def test_measurement_sensor_invalido():
    """PE: sensor_ok com valor não booleano lança MeasurementValidationError (TU-106)."""
    with pytest.raises(MeasurementValidationError):
        create_measurement({"batch_id": 1, "temp": 23.0, "humidity": 60.0,
                            "luminosity": 15000, "sensor_ok": "sim"})
