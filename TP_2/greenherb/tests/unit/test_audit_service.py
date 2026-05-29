import pytest

from api.services.audit_service import is_auditable_action


# ---------------------------------------------------------------------------
# TU-148 a TU-152 — PE: operações auditáveis vs. não auditáveis
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, action, esperado",
    [
        ("TU-148", "create_batch",  True),   # PE: operação de escrita → auditável
        ("TU-149", "resolve_alert", True),   # PE: operação de escrita → auditável
        ("TU-150", "close_batch",   True),   # PE: operação de escrita → auditável
        ("TU-151", "get_batches",   False),  # PE: operação de leitura → não auditável
        ("TU-152", "get_herbs",     False),  # PE: operação de leitura → não auditável
    ],
)
def test_is_auditable_action(test_id, action, esperado):
    """PE: is_auditable_action — operações de escrita auditadas; leituras não auditadas (TU-148 a TU-152)."""
    assert is_auditable_action(action) == esperado
