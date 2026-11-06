"""Serviço de monitorização que liga o sensor de temperatura à geração
de alertas e ao envio de notificações.

Recebe os gateways por injeção de dependências, o que permite substituí-los
por duplos de teste (Stub para o sensor, Mock para as notificações).
"""

from api.gateways.notification_gateway import NotificationError, NotificationGateway
from api.gateways.temperature_sensor_gateway import (
    SensorUnavailableError,
    TemperatureSensorGateway,
)


DEFAULT_TEMP_MIN = 18.0
DEFAULT_TEMP_MAX = 28.0
# Desvio (°C) a partir do qual o alerta passa de Informativo a Crítico.
CRITICAL_DEVIATION = 7.0


def classify_temperature(temp, temp_min=DEFAULT_TEMP_MIN, temp_max=DEFAULT_TEMP_MAX):
    """Classifica uma leitura de temperatura.

    Returns: "Crítico" | "Informativo" | None
    """
    if temp_min <= temp <= temp_max:
        return None
    deviation = (temp_min - temp) if temp < temp_min else (temp - temp_max)
    return "Crítico" if deviation > CRITICAL_DEVIATION else "Informativo"


class MonitoringService:
    def __init__(
        self,
        sensor_gateway: TemperatureSensorGateway,
        notification_gateway: NotificationGateway,
        temp_min: float = DEFAULT_TEMP_MIN,
        temp_max: float = DEFAULT_TEMP_MAX,
    ):
        self._sensor = sensor_gateway
        self._notifier = notification_gateway
        self._temp_min = temp_min
        self._temp_max = temp_max

    def monitor_batch(self, batch_id: int) -> dict:
        """Lê a temperatura do lote, classifica um alerta e — apenas para
        alertas Críticos — envia uma notificação.

        Devolve um resumo com o estado da operação. Nunca rebenta: se o sensor
        ou o serviço de notificações falharem, o erro é refletido no resultado.
        """
        try:
            temp = self._sensor.read_temperature(batch_id)
        except SensorUnavailableError:
            return {
                "status": "sensor_unavailable",
                "temperature": None,
                "alert": None,
                "notified": False,
            }

        level = classify_temperature(temp, self._temp_min, self._temp_max)

        notified = False
        if level == "Crítico":
            try:
                self._notifier.send(
                    recipient="responsavel@greenherb.pt",
                    subject=f"[CRÍTICO] Lote {batch_id}",
                    body=f"Temperatura crítica detetada: {temp} °C.",
                )
                notified = True
            except NotificationError:
                # O serviço externo falhou, mas a app não pode rebentar.
                notified = False

        return {
            "status": "ok",
            "temperature": temp,
            "alert": level,
            "notified": notified,
        }
