import pytest

from api.services.automation_service import AutomationDecisionError, decide_automation


# ---------------------------------------------------------------------------
# TU-127 a TU-131 — PE: motor de automação
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, mode, rule_active, measurement_recent, esperado",
    [
        ("TU-127", "Automático", True,  True,  "executada"),  # PE: modo automático, tudo activo
        ("TU-128", "Manual",     True,  True,  "sugerida"),   # PE: modo manual, tudo activo
        ("TU-129", "Automático", False, True,  "ignorada"),   # PE: regra inativa
        ("TU-130", "Manual",     True,  False, "ignorada"),   # PE: medição não recente
        ("TU-131", "Híbrido",    True,  True,  "erro"),       # PE: modo inválido
    ],
)
def test_decide_automation(test_id, mode, rule_active, measurement_recent, esperado):
    """PE: decide_automation — classes executada / sugerida / ignorada / erro (TU-127 a TU-131)."""
    if esperado == "erro":
        with pytest.raises(AutomationDecisionError):
            decide_automation(mode, rule_active, measurement_recent)
    else:
        assert decide_automation(mode, rule_active, measurement_recent) == esperado
