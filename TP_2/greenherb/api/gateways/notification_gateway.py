"""Gateway para o serviço externo de notificações.

Em produção, a implementação real enviaria a notificação por e-mail,
SMS ou push para um serviço externo. Aqui definimos a interface; os
testes usam um Mock que regista as chamadas para verificação posterior.
"""

from abc import ABC, abstractmethod


class NotificationError(RuntimeError):
    """Levantada quando o envio da notificação falha."""


class NotificationGateway(ABC):
    """Interface do gateway de envio de notificações."""

    @abstractmethod
    def send(self, recipient: str, subject: str, body: str) -> bool:
        """Envia uma notificação.

        Returns:
            True se a notificação foi aceite pelo serviço externo.
        Raises:
            NotificationError: se o envio falhar.
        """
        raise NotImplementedError
