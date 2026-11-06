import pytest

from api.services.monitoring_service import MonitoringService
from tests.doubles.notification_gateway_mock import NotificationGatewayMock
from tests.doubles.temperature_sensor_stub import TemperatureSensorStub


# ---------------------------------------------------------------------------
# Mock do gateway de notificações (duplo de teste — fora da matriz)
# ---------------------------------------------------------------------------

def test_alerta_critico_envia_notificacao():
    """Mock: alerta Crítico envia exatamente uma notificação com os parâmetros certos."""
    sensor = TemperatureSensorStub(temperature=40.0)   # 12 °C acima → Crítico
    notifier = NotificationGatewayMock()
    service = MonitoringService(sensor, notifier)

    result = service.monitor_batch(batch_id=7)

    assert result["alert"] == "Crítico"
    assert result["notified"] is True
    # Verificação de comportamento (próprio dos mocks): chamado uma vez...
    assert notifier.send_count == 1
    call = notifier.last_call()
    # ...e com os parâmetros corretos: destinatário, tipo de alerta e mensagem.
    assert call["recipient"] == "responsavel@greenherb.pt"   # destinatário
    assert "[CRÍTICO]" in call["subject"]                    # tipo de alerta
    assert "Lote 7" in call["subject"]                       # lote afetado
    assert "40" in call["body"]                              # leitura na mensagem
    assert "Temperatura crítica" in call["body"]             # corpo da mensagem


def test_dentro_dos_limites_nao_envia_notificacao():
    """Mock: leitura dentro dos limites não gera alerta nem envia notificação."""
    sensor = TemperatureSensorStub(temperature=23.0)   # dentro de [18, 28] → sem alerta
    notifier = NotificationGatewayMock()
    service = MonitoringService(sensor, notifier)

    result = service.monitor_batch(batch_id=1)

    assert result["alert"] is None
    assert result["notified"] is False
    assert notifier.was_called is False
    assert notifier.send_count == 0


def test_alerta_informativo_nao_envia_notificacao():
    """Mock: alerta Informativo NÃO envia notificação."""
    sensor = TemperatureSensorStub(temperature=31.0)   # 3 °C acima → Informativo
    notifier = NotificationGatewayMock()
    service = MonitoringService(sensor, notifier)

    result = service.monitor_batch(batch_id=1)

    assert result["alert"] == "Informativo"
    assert result["notified"] is False
    assert notifier.was_called is False
    assert notifier.send_count == 0


def test_falha_no_envio_nao_rebenta():
    """Mock: se o gateway de notificações falhar, a app não rebenta."""
    sensor = TemperatureSensorStub(temperature=40.0)   # Crítico → tenta notificar
    notifier = NotificationGatewayMock(should_fail=True)
    service = MonitoringService(sensor, notifier)

    result = service.monitor_batch(batch_id=1)

    # O alerta foi gerado, mas a notificação falhou — sem exceção propagada.
    assert result["alert"] == "Crítico"
    assert result["notified"] is False


# ---------------------------------------------------------------------------
# Fronteira do limiar Crítico↔Informativo (CRITICAL_DEVIATION = 7 °C)
# O nível depende do DESVIO face ao limite, não da direção.
# ---------------------------------------------------------------------------

def test_fronteira_desvio_7_informativo_nao_notifica():
    """TU-178 (Mock + VL): desvio = 7 °C (35°C) → Informativo → notificação NÃO enviada."""
    sensor = TemperatureSensorStub(temperature=35.0)   # 35-28 = 7; 7 não é > 7 → Informativo
    notifier = NotificationGatewayMock()
    service = MonitoringService(sensor, notifier)

    result = service.monitor_batch(batch_id=1)

    assert result["alert"] == "Informativo"
    assert result["notified"] is False
    assert notifier.was_called is False
    assert notifier.send_count == 0


def test_fronteira_desvio_8_critico_notifica():
    """TU-179 (Mock + VL): desvio = 8 °C (36°C) → Crítico → notificação enviada."""
    sensor = TemperatureSensorStub(temperature=36.0)   # 36-28 = 8; 8 > 7 → Crítico
    notifier = NotificationGatewayMock()
    service = MonitoringService(sensor, notifier)

    result = service.monitor_batch(batch_id=1)

    assert result["alert"] == "Crítico"
    assert result["notified"] is True
    assert notifier.send_count == 1
