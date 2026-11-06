from api.services.mock_service import create_mock, list_mock


VALID_FORMATS = {"CSV", "Excel"}


class ReportValidationError(ValueError):
    status_code = 400


def validate_report_format(format_str):
    """Validate report export format."""
    if format_str is None:
        raise ReportValidationError("format is required.")
    if format_str not in VALID_FORMATS:
        raise ReportValidationError(
            f"format must be one of: {', '.join(sorted(VALID_FORMATS))}."
        )


def list_reports():
    return list_mock("reports")


def create_report(payload):
    return create_mock("reports", payload)
