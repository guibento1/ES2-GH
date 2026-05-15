from app.services.audit_service import list_audit_logs


def get_audit_logs():
    return list_audit_logs()
