from api.services.mock_service import create_mock, list_mock


ALERT_LEVELS = ("Informativo", "Aviso", "Crítico")


class AlertClassificationError(ValueError):
    """Raised when alert inputs are invalid."""
    status_code = 400


def classify_alert(temp, humidity, limits, sensor_ok):
    """
    Classify an environmental alert based on sensor readings vs plan limits.

    Compound decision (MC/DC target):
        resultado = (C1 OR C2) AND C3
        C1: temp    > limits['temp_max']
        C2: humidity < limits['humidity_min']
        C3: sensor_ok

    Returns:
        "Crítico"     — C1 AND C2 AND C3  (both limits violated, sensor active)
        "Aviso"       — (C1 XOR C2) AND C3 (one limit violated, sensor active)
        None          — sensor inactive OR all readings within limits
    """
    if not isinstance(sensor_ok, bool):
        raise AlertClassificationError("sensor_ok must be a boolean.")
    if temp is None or humidity is None:
        raise AlertClassificationError("temp and humidity are required.")
    if "temp_max" not in limits or "humidity_min" not in limits:
        raise AlertClassificationError("limits must contain temp_max and humidity_min.")

    c1 = temp > limits["temp_max"]
    c2 = humidity < limits["humidity_min"]
    c3 = sensor_ok

    if not c3:
        return None

    if c1 and c2:
        return "Crítico"
    if c1 or c2:
        return "Aviso"
    return None


def list_alerts():
    return list_mock("alerts")


def create_alert(payload):
    return create_mock("alerts", payload)
