from api.data import memory_store


class AlertClassificationError(ValueError):
    status_code = 400


class AlertNotFoundError(ValueError):
    status_code = 404


class AlertActionError(ValueError):
    status_code = 422

MIN_JUSTIFICATION_LEN = 10
MAX_JUSTIFICATION_LEN = 500


def classify_alert(temp, humidity, limits, sensor_ok):
    """
    Compound decision (MC/DC):
        resultado = (C1 OR C2) AND C3
        C1: temp     > limits['temp_max']
        C2: humidity < limits['humidity_min']
        C3: sensor_ok

    Returns: "Crítico" | "Aviso" | None
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


def resolve_alert(alert_id, action, justification=None):
    """
    Resolve or ignore an alert.
    - action "resolvido": justification optional
    - action "ignorado":  justification required (10–500 chars)
    """
    if action not in ("resolvido", "ignorado"):
        raise AlertActionError("action must be 'resolvido' or 'ignorado'.")

    alert = memory_store.find_alert_by_id(alert_id)
    if alert is None:
        raise AlertNotFoundError(f"Alerta {alert_id} não encontrado.")
    if alert["state"] != "pendente":
        raise AlertActionError(f"Alerta já está '{alert['state']}'; não pode ser alterado.")

    if action == "ignorado":
        if not justification or not isinstance(justification, str):
            raise AlertActionError("Justificação obrigatória para ignorar um alerta.")
        j = justification.strip()
        if len(j) < MIN_JUSTIFICATION_LEN:
            raise AlertActionError(
                f"Justificação demasiado curta (mínimo {MIN_JUSTIFICATION_LEN} caracteres)."
            )
        if len(j) > MAX_JUSTIFICATION_LEN:
            raise AlertActionError(
                f"Justificação demasiado longa (máximo {MAX_JUSTIFICATION_LEN} caracteres)."
            )

    return memory_store.update_alert(alert_id, {
        "state": action,
        "justification": justification,
    })


def list_alerts():
    return memory_store.list_alerts()


def create_alert(payload):
    return memory_store.add_alert(payload)
