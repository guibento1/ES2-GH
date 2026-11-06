"""Mock do gateway de notificações.

Um MOCK é o duplo adequado aqui porque precisamos de **verificar o comportamento**:
saber se a notificação FOI enviada, quantas vezes e com que parâmetros — e não
apenas o valor devolvido. O mock regista todas as chamadas a send() para que o
teste possa fazer asserções sobre elas.
"""

from api.gateways.notification_gateway import NotificationError, NotificationGateway


class NotificationGatewayMock(NotificationGateway):
    def __init__(self, should_fail: bool = False):
        self.should_fail = should_fail
        self.calls = []   # regista cada chamada como dict(recipient, subject, body)

    def send(self, recipient: str, subject: str, body: str) -> bool:
        if self.should_fail:
            raise NotificationError("Serviço de notificações indisponível.")
        self.calls.append({"recipient": recipient, "subject": subject, "body": body})
        return True

    # --- métodos de verificação usados pelos testes ---

    @property
    def send_count(self) -> int:
        return len(self.calls)

    @property
    def was_called(self) -> bool:
        return len(self.calls) > 0

    def last_call(self) -> dict:
        return self.calls[-1] if self.calls else None
