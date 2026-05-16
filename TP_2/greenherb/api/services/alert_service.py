from api.data import memory_store


class AlertClassificationError(ValueError):
    status_code = 400


class AlertNotFoundError(ValueError):
    status_code = 404


class AlertActionError(ValueError):
    status_code = 422


MIN_JUSTIFICATION_LEN = 10
MAX_JUSTIFICATION_LEN = 500


def classify_alert(temp, humidity, luminosity, limits, sensor_ok):
    """Returns "Crítico" | "Aviso" | "Informativo" | None."""
    if not isinstance(sensor_ok, bool):
        raise AlertClassificationError("sensor_ok must be a boolean.")
    if any(v is None for v in (temp, humidity, luminosity)):
        raise AlertClassificationError("temp, humidity and luminosity are required.")
    required = ("temp_min", "temp_max", "humidity_min", "humidity_max",
                "luminosity_min", "luminosity_max")
    if any(k not in limits for k in required):
        raise AlertClassificationError("limits must contain all 6 boundary keys.")

    if not sensor_ok:
        return None

    temp_out = temp < limits["temp_min"] or temp > limits["temp_max"]
    hum_out = humidity < limits["humidity_min"] or humidity > limits["humidity_max"]
    lux_out = luminosity < limits["luminosity_min"] or luminosity > limits["luminosity_max"]

    if temp_out and hum_out:
        return "Crítico"
    if temp_out or hum_out:
        return "Aviso"
    if lux_out:
        return "Informativo"
    return None


def resolve_alert(alert_id, action, justification=None):
    """Resolve or ignore an alert.
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
