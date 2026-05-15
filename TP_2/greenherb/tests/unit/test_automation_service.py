"""
Testes de unidade — Sprint 3
Módulo: api.services.automation_service  (TU-76 a TU-79)

Técnica: Cobertura de Condições Múltiplas + MC/DC

Decisão composta:
  C1: mode == "Automático"
  C2: rule_active
  C3: measurement_recent

Lógica:
  NOT C2 OR NOT C3  →  "ignorada"   (regra inactiva ou medição não recente)
  C1=T, C2=T, C3=T  →  "executada"  (modo automático, tudo activo)
  C1=F, C2=T, C3=T  →  "sugerida"   (modo manual, tudo activo)

TU-76  Automático + regra ativa + medição recente   →  "executada"
TU-77  Manual     + regra ativa + medição recente   →  "sugerida"
TU-78  Qualquer   + regra inativa                   →  "ignorada"
TU-79  Qualquer   + medição não recente              →  "ignorada"
"""

import pytest

from api.services.automation_service import AutomationDecisionError, decide_automation


@pytest.mark.parametrize(
    "test_id, mode,        rule_active, measurement_recent, esperado",
    [
        # TU-76: C1=T, C2=T, C3=T → "executada"
        ("TU-76", "Automático", True,  True,  "executada"),

        # TU-77: C1=F, C2=T, C3=T → "sugerida"
        ("TU-77", "Manual",     True,  True,  "sugerida"),

        # TU-78: C2=F (regra inativa) → "ignorada" independentemente de C1 e C3
        ("TU-78", "Automático", False, True,  "ignorada"),

        # TU-79: C3=F (medição não recente) → "ignorada" independentemente de C1 e C2
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
