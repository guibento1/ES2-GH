import pytest

from api.services.monitoring_service import MonitoringService
from tests.doubles.notification_gateway_mock import NotificationGatewayMock
from tests.doubles.temperature_sensor_stub import TemperatureSensorStub


def _service(temperature=None, available=True):
    """Monta o serviço com um sensor-stub controlado e um mock de notificações."""
    sensor = TemperatureSensorStub(temperature=temperature, available=available)
    notifier = NotificationGatewayMock()
    return MonitoringService(sensor, notifier)


# ---------------------------------------------------------------------------
# Stub do sensor de temperatura (duplo de teste — fora da matriz)
# ---------------------------------------------------------------------------

def test_temperatura_dentro_dos_limites_sem_alerta():
    """Stub: temperatura dentro dos limites não gera alerta."""
    service = _service(temperature=23.0)
    result = service.monitor_batch(batch_id=1)
    assert result["status"] == "ok"
    assert result["temperature"] == 23.0
    assert result["alert"] is None


def test_temperatura_abaixo_do_minimo_gera_alerta():
    """Stub: temperatura abaixo do mínimo gera alerta."""
    service = _service(temperature=5.0)   # 13 °C abaixo de 18 → Crítico
    result = service.monitor_batch(batch_id=1)
    assert result["alert"] == "Crítico"


def test_temperatura_acima_do_maximo_gera_alerta():
    """Stub: temperatura acima do máximo gera alerta."""
    service = _service(temperature=31.0)  # 3 °C acima de 28 → Informativo
    result = service.monitor_batch(batch_id=1)
    assert result["alert"] == "Informativo"


def test_sensor_indisponivel_nao_rebenta():
    """Stub: sensor indisponível devolve estado controlado sem rebentar."""
    service = _service(available=False)
    result = service.monitor_batch(batch_id=1)
    assert result["status"] == "sensor_unavailable"
    assert result["alert"] is None
    assert result["temperature"] is None
