import pytest

from api.services.batch_service import (
    BatchCalculationError,
    BatchStateError,
    calculate_productivity,
    transition_batch_state,
)


@pytest.mark.parametrize(
    "test_id, current_state, has_losses, end_date_set, esperado",
    [
        ("TU-65", "ativo",        False, True,  "concluído"),
        ("TU-66", "ativo",        True,  True,  "comprometido"),
        ("TU-67", "ativo",        False, False, "erro"),
        ("TU-68", "concluído",    False, True,  "erro"),
        ("TU-69", "comprometido", True,  True,  "erro"),
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


@pytest.mark.parametrize(
    "test_id, planned, actual, losses, esperado",
    [
        ("TU-71", 100, 100,  0,  100.0),
        ("TU-72", 100, 100, 20,   80.0),
        ("TU-73", 100,  60,  0,   60.0),
        ("TU-74", 100,  50, 60,  "erro"),
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
