import pytest

from api.services.automation_service import AutomationDecisionError, decide_automation


@pytest.mark.parametrize(
    "test_id, mode,        rule_active, measurement_recent, esperado",
    [
        ("TU-76", "Automático", True,  True,  "executada"),
        ("TU-77", "Manual",     True,  True,  "sugerida"),
        ("TU-78", "Automático", False, True,  "ignorada"),
        ("TU-79", "Manual",     True,  False, "ignorada"),
    ],
)
def test_decide_automation(test_id, mode, rule_active, measurement_recent, esperado):
    """MC/DC: motor de automação — decide_automation (TU-76 a TU-79)."""
    result = decide_automation(mode, rule_active, measurement_recent)
    assert result == esperado, (
        f"[{test_id}] mode={mode}, rule_active={rule_active}, "
        f"measurement_recent={measurement_recent} → esperado '{esperado}', obtido '{result}'"
    )


def test_decide_automation_modo_invalido():
    """PE: modo desconhecido lança AutomationDecisionError."""
    with pytest.raises(AutomationDecisionError):
        decide_automation("Semiautomático", True, True)
