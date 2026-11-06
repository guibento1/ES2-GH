import pytest

from api.services.report_service import ReportValidationError, validate_report_format


# ---------------------------------------------------------------------------
# TU-143 a TU-147 — PE: formato de relatório
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, fmt, esperado",
    [
        ("TU-143", "CSV",   "ok"),    # PE: formato válido
        ("TU-144", "Excel", "ok"),    # PE: formato válido
        ("TU-145", "PDF",   "erro"),  # PE: formato inválido
        ("TU-146", "JSON",  "erro"),  # PE: formato inválido
        ("TU-147", None,    "erro"),  # PE: formato ausente
    ],
)
def test_report_format(test_id, fmt, esperado):
    """PE: validate_report_format — CSV e Excel aceites; outros formatos rejeitados (TU-143 a TU-147)."""
    if esperado == "erro":
        with pytest.raises(ReportValidationError):
            validate_report_format(fmt)
    else:
        validate_report_format(fmt)
