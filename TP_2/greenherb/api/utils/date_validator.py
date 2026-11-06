import re
from datetime import date

_YYYY_MM_DD = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class DateValidationError(ValueError):
    status_code = 400


def validate_date(date_str):
    """Validates that date_str is a valid calendar date strictly in YYYY-MM-DD format."""
    if date_str is None:
        return
    if not isinstance(date_str, str):
        raise DateValidationError("Data deve ser uma string no formato YYYY-MM-DD.")
    if not _YYYY_MM_DD.match(date_str):
        raise DateValidationError(
            f"Formato de data inválido: '{date_str}'. Use YYYY-MM-DD."
        )
    try:
        date.fromisoformat(date_str)
    except ValueError:
        raise DateValidationError(
            f"Data inexistente: '{date_str}'."
        )
