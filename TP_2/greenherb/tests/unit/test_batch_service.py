import pytest

from api.services.batch_service import (
    BatchCalculationError,
    BatchStateError,
    BatchValidationError,
    calculate_productivity,
    transition_batch_state,
    validate_batch,
)


# ---------------------------------------------------------------------------
# TU-68 a TU-73 — PE: transições de estado do lote
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, current_state, has_losses, end_date_set, esperado",
    [
        ("TU-68", "ativo",        False, True,  "concluído"),    # PE: ativo + sem perdas → concluído
        ("TU-69", "ativo",        True,  True,  "comprometido"), # PE: ativo + com perdas → comprometido
        ("TU-70", "ativo",        False, False, "erro"),         # PE: ativo sem data → erro
        ("TU-71", "concluído",    False, True,  "erro"),         # PE: estado terminal
        ("TU-72", "comprometido", True,  True,  "erro"),         # PE: estado terminal
        ("TU-73", "suspenso",     False, True,  "erro"),         # PE: estado inválido
    ],
)
def test_transition_batch_state(test_id, current_state, has_losses, end_date_set, esperado):
    """PE: transition_batch_state — estados válidos e inválidos (TU-68 a TU-73)."""
    if esperado == "erro":
        with pytest.raises(BatchStateError):
            transition_batch_state(current_state, has_losses, end_date_set)
    else:
        assert transition_batch_state(current_state, has_losses, end_date_set) == esperado


# ---------------------------------------------------------------------------
# TU-74 a TU-78 — PE: cálculo de produtividade
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, planned, actual, losses, esperado",
    [
        ("TU-74", 100, 100,  0,  100.0),  # PE: sem perdas, colheita total → 100%
        ("TU-75", 100, 100, 20,   80.0),  # PE: com perdas → 80%
        ("TU-76", 100,  60,  0,   60.0),  # PE: colheita parcial → 60%
        ("TU-77", 100,  50, 60,  "erro"), # PE: perdas > colheita → erro
        ("TU-78",   0, 100,  0,  "erro"), # PE: planned=0 → divisão por zero
    ],
)
def test_calculate_productivity(test_id, planned, actual, losses, esperado):
    """PE: calculate_productivity — classes válidas e inválidas (TU-74 a TU-78)."""
    if esperado == "erro":
        with pytest.raises(BatchCalculationError):
            calculate_productivity(planned, actual, losses)
    else:
        assert calculate_productivity(planned, actual, losses) == pytest.approx(esperado)


# ---------------------------------------------------------------------------
# TU-79 a TU-82 — PE: validação de lote (validate_batch)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, payload, esperado",
    [
        ("TU-79", {"herb_id": 1, "planned_qty": 100.0},  "ok"),    # PE: payload válido
        ("TU-80", {"planned_qty": 100.0},                "erro"),  # PE: herb_id em falta
        ("TU-81", {"herb_id": 1, "planned_qty": 0},      "erro"),  # PE: planned_qty zero
        ("TU-82", {"herb_id": 1, "planned_qty": -10},    "erro"),  # PE: planned_qty negativo
    ],
)
def test_validate_batch(test_id, payload, esperado):
    """PE: validate_batch — campos obrigatórios e valores válidos (TU-79 a TU-82)."""
    if esperado == "erro":
        with pytest.raises(BatchValidationError):
            validate_batch(payload)
    else:
        validate_batch(payload)
