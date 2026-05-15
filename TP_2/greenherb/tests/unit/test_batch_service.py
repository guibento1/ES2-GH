"""
Testes de unidade — Sprint 3
Módulo: api.services.batch_service  (TU-65 a TU-75)

Cobrem duas funções:
  A) transition_batch_state  — transições de estado do lote        PE + MC/DC
  B) calculate_productivity  — cálculo de produtividade            PE + VL

Transições permitidas:
  ativo  + end_date + sem perdas  →  "concluído"
  ativo  + end_date + com perdas  →  "comprometido"
  ativo  + sem end_date           →  BatchStateError
  concluído / comprometido        →  BatchStateError (estado terminal)
  estado inválido                 →  BatchStateError

Produtividade = (actual_qty - losses) / planned_qty × 100
"""

import pytest

from api.services.batch_service import (
    BatchCalculationError,
    BatchStateError,
    calculate_productivity,
    transition_batch_state,
)


# ===========================================================================
# A) transition_batch_state — TU-65 a TU-70
# ===========================================================================

@pytest.mark.parametrize(
    "test_id, current_state, has_losses, end_date_set, esperado",
    [
        # TU-65: ativo + sem perdas + data definida → concluído
        ("TU-65", "ativo",        False, True,  "concluído"),

        # TU-66: ativo + com perdas + data definida → comprometido
        ("TU-66", "ativo",        True,  True,  "comprometido"),

        # TU-67: ativo + sem data de conclusão → erro (C3=False)
        ("TU-67", "ativo",        False, False, "erro"),

        # TU-68: concluído → não pode transicionar (estado terminal)
        ("TU-68", "concluído",    False, True,  "erro"),

        # TU-69: comprometido → não pode transicionar (estado terminal)
        ("TU-69", "comprometido", True,  True,  "erro"),

        # TU-70: estado inválido ("suspenso") → erro imediato
        ("TU-70", "suspenso",     False, True,  "erro"),
    ],
)
def test_transition_batch_state(test_id, current_state, has_losses, end_date_set, esperado):
    """PE + MC/DC: transições de estado do lote (TU-65 a TU-70)."""
    if esperado == "erro":
        with pytest.raises(BatchStateError):
            transition_batch_state(current_state, has_losses, end_date_set)
    else:
        result = transition_batch_state(current_state, has_losses, end_date_set)
        assert result == esperado, f"[{test_id}] esperado '{esperado}', obtido '{result}'"


# ===========================================================================
# B) calculate_productivity — TU-71 a TU-75
# ===========================================================================

@pytest.mark.parametrize(
    "test_id, planned, actual, losses, esperado",
    [
        # TU-71: sem perdas, colheita total → 100%
        ("TU-71", 100, 100,  0,  100.0),

        # TU-72: com perdas parciais → produtividade < 100%
        ("TU-72", 100, 100, 20,   80.0),

        # TU-73: colheita parcial sem perdas → produtividade proporcional
        ("TU-73", 100,  60,  0,   60.0),

        # TU-74: perdas superiores à colheita → erro
        ("TU-74", 100,  50, 60,  "erro"),

        # TU-75: planned_qty = 0 → divisão por zero → erro
        ("TU-75",   0, 100,  0,  "erro"),
    ],
)
def test_calculate_productivity(test_id, planned, actual, losses, esperado):
    """PE + VL: cálculo de produtividade do lote (TU-71 a TU-75)."""
    if esperado == "erro":
        with pytest.raises(BatchCalculationError):
            calculate_productivity(planned, actual, losses)
    else:
        result = calculate_productivity(planned, actual, losses)
        assert result == pytest.approx(esperado), (
            f"[{test_id}] esperado {esperado}%, obtido {result}%"
        )
