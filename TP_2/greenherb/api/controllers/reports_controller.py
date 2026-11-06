from fastapi import HTTPException, status

from api.services.report_service import ReportValidationError, list_reports, validate_report_format


def get_reports(format: str = None):
    if format is not None:
        try:
            validate_report_format(format)
        except ReportValidationError as exc:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    return list_reports()
