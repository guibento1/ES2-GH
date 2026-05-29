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
# TU-91 a TU-95 — VL: temperatura [18, 28] °C
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, temp, alerta_esperado",
    [
        ("TU-91", 17, True),   # VL: abaixo do limite inferior (17 < 18) → alerta
        ("TU-92", 18, False),  # VL: limite inferior exacto → sem alerta
        ("TU-93", 23, False),  # VL: valor nominal interior → sem alerta
        ("TU-94", 28, False),  # VL: limite superior exacto → sem alerta
        ("TU-95", 29, True),   # VL: acima do limite superior (29 > 28) → alerta
    ],
)
def test_measurement_temperatura_vl(test_id, temp, alerta_esperado, store_medicoes):
    """VL: temperatura [18, 28] °C — alerta gerado fora dos limites (TU-91 a TU-95)."""
    result = create_measurement({"batch_id": 1, "temp": temp, "humidity": 60.0,
                                 "luminosity": 15000, "sensor_ok": True})
    assert (result["alert"] is not None) == alerta_esperado


# ---------------------------------------------------------------------------
# TU-96 a TU-100 — VL: humidade [40, 80] %
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, hum, alerta_esperado",
    [
        ("TU-96", 39, True),   # VL: abaixo do limite inferior (39 < 40) → alerta
        ("TU-97", 40, False),  # VL: limite inferior exacto → sem alerta
        ("TU-98", 60, False),  # VL: valor nominal interior → sem alerta
        ("TU-99", 80, False),  # VL: limite superior exacto → sem alerta
        ("TU-100", 81, True),   # VL: acima do limite superior (81 > 80) → alerta
    ],
)
def test_measurement_humidade_vl(test_id, hum, alerta_esperado, store_medicoes):
    """VL: humidade [40, 80] % — alerta gerado fora dos limites (TU-96 a TU-100)."""
    result = create_measurement({"batch_id": 1, "temp": 23.0, "humidity": hum,
                                 "luminosity": 15000, "sensor_ok": True})
    assert (result["alert"] is not None) == alerta_esperado


# ---------------------------------------------------------------------------
# TU-101 a TU-105 — VL: luminosidade [5000, 25000] lux
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, lux, alerta_esperado",
    [
        ("TU-101",  4999, True),   # VL: abaixo do limite inferior (4999 < 5000) → alerta
        ("TU-102",  5000, False),  # VL: limite inferior exacto → sem alerta
        ("TU-103", 15000, False),  # VL: valor nominal interior → sem alerta
        ("TU-104", 25000, False),  # VL: limite superior exacto → sem alerta
        ("TU-105", 25001, True),   # VL: acima do limite superior (25001 > 25000) → alerta
    ],
)
def test_measurement_luminosidade_vl(test_id, lux, alerta_esperado, store_medicoes):
    """VL: luminosidade [5000, 25000] lux — alerta gerado fora dos limites (TU-101 a TU-105)."""
    result = create_measurement({"batch_id": 1, "temp": 23.0, "humidity": 60.0,
                                 "luminosity": lux, "sensor_ok": True})
    assert (result["alert"] is not None) == alerta_esperado


# ---------------------------------------------------------------------------
# TU-106 a TU-107 — PE: sensor_ok
# ---------------------------------------------------------------------------

def test_measurement_sensor_off_sem_alerta(store_medicoes):
    """PE: sensor_ok=False → sem alerta mesmo com leituras fora dos limites (TU-106)."""
    result = create_measurement({"batch_id": 1, "temp": 35.0, "humidity": 20.0,
                                 "luminosity": 1000, "sensor_ok": False})
    assert result["alert"] is None


def test_measurement_sensor_invalido():
    """PE: sensor_ok com valor não booleano lança MeasurementValidationError (TU-107)."""
    with pytest.raises(MeasurementValidationError):
        create_measurement({"batch_id": 1, "temp": 23.0, "humidity": 60.0,
                            "luminosity": 15000, "sensor_ok": "sim"})
