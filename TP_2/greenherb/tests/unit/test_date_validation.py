import pytest

from api.utils.date_validator import DateValidationError, validate_date


# ---------------------------------------------------------------------------
# TU-57 a TU-67 — PE: formatos de data em /plans, /batches, /tasks
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, date_str, esperado",
    [
        ("TU-57", "2026-05-16",  "ok"),    # PE: formato válido YYYY-MM-DD
        ("TU-58", "16-05-2026",  "erro"),  # PE: DD-MM-YYYY (formato inválido)
        ("TU-59", "05-16-2026",  "erro"),  # PE: MM-DD-YYYY (formato inválido)
        ("TU-60", "16/05/2026",  "erro"),  # PE: DD/MM/YYYY com barras
        ("TU-61", "2026/05/16",  "erro"),  # PE: YYYY/MM/DD com barras
        ("TU-62", "20260516",    "erro"),  # PE: sem separadores
        ("TU-63", "amanha",      "erro"),  # PE: string que não é data
        ("TU-64", "16 maio 2026","erro"),  # PE: data por extenso
        ("TU-65", "2026-13-01",  "erro"),  # PE: mês inexistente (13)
        ("TU-66", "2026-02-30",  "erro"),  # PE: dia inexistente (fev 30)
        ("TU-67", "2026-00-01",  "erro"),  # PE: mês inexistente (00)
    ],
)
def test_validate_date(test_id, date_str, esperado):
    """PE: validate_date — formato YYYY-MM-DD válido; outros formatos e datas inexistentes rejeitados (TU-57 a TU-67)."""
    if esperado == "erro":
        with pytest.raises(DateValidationError):
            validate_date(date_str)
    else:
        validate_date(date_str)
