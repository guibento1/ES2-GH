from app.services.report_service import create_report, list_reports


def get_reports():
    return list_reports()


def create_report_endpoint(payload):
    return create_report(payload)
