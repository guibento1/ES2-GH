import pytest

from api.services.report_service import ReportValidationError, validate_report_format


# ---------------------------------------------------------------------------
# TU-142 a TU-146 — PE: formato de relatório
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, fmt, esperado",
    [
        ("TU-142", "CSV",   "ok"),    # PE: formato válido
        ("TU-143", "Excel", "ok"),    # PE: formato válido
        ("TU-144", "PDF",   "erro"),  # PE: formato inválido
        ("TU-145", "JSON",  "erro"),  # PE: formato inválido
        ("TU-146", None,    "erro"),  # PE: formato ausente
    ],
)
def test_report_format(test_id, fmt, esperado):
    """PE: validate_report_format — CSV e Excel aceites; outros formatos rejeitados (TU-142 a TU-146)."""
    if esperado == "erro":
        with pytest.raises(ReportValidationError):
            validate_report_format(fmt)
    else:
        validate_report_format(fmt)
