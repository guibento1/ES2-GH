"""Stub do sensor de temperatura.

Um STUB é o duplo adequado aqui porque só precisamos de **controlar o valor
devolvido** (ou forçar uma falha) — não nos interessa verificar como o gateway
foi chamado. O stub devolve sempre a temperatura pré-configurada.
"""

from api.gateways.temperature_sensor_gateway import (
    SensorUnavailableError,
    TemperatureSensorGateway,
)


class TemperatureSensorStub(TemperatureSensorGateway):
    def __init__(self, temperature: float = None, available: bool = True):
        self._temperature = temperature
        self._available = available

    def read_temperature(self, batch_id: int) -> float:
        if not self._available:
            raise SensorUnavailableError(f"Sensor do lote {batch_id} indisponível.")
        return self._temperature
