"""Gateway para o sensor de temperatura da estufa.

Em produção, a implementação real leria de hardware/API externa
(ex.: um sensor físico ou um serviço HTTP de telemetria). Aqui definimos
a interface; os testes usam um Stub que devolve valores controlados.
"""

from abc import ABC, abstractmethod


class SensorUnavailableError(RuntimeError):
    """Levantada quando o sensor está indisponível ou falha a leitura."""


class TemperatureSensorGateway(ABC):
    """Interface do gateway de leitura de temperatura."""

    @abstractmethod
    def read_temperature(self, batch_id: int) -> float:
        """Devolve a temperatura atual (°C) do lote indicado.

        Raises:
            SensorUnavailableError: se o sensor não responder.
        """
        raise NotImplementedError
