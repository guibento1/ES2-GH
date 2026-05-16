import pytest

from api.services.audit_service import is_auditable_action


# ---------------------------------------------------------------------------
# TU-147 a TU-151 — PE: operações auditáveis vs. não auditáveis
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, action, esperado",
    [
        ("TU-147", "create_batch",  True),   # PE: operação de escrita → auditável
        ("TU-148", "resolve_alert", True),   # PE: operação de escrita → auditável
        ("TU-149", "close_batch",   True),   # PE: operação de escrita → auditável
        ("TU-150", "get_batches",   False),  # PE: operação de leitura → não auditável
        ("TU-151", "get_herbs",     False),  # PE: operação de leitura → não auditável
    ],
)
def test_is_auditable_action(test_id, action, esperado):
    """PE: is_auditable_action — operações de escrita auditadas; leituras não auditadas (TU-147 a TU-151)."""
    assert is_auditable_action(action) == esperado
