from app.services.alert_service import create_alert, list_alerts


def get_alerts():
    return list_alerts()


def create_alert_endpoint(payload):
    return create_alert(payload)
