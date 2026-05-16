from api.data import memory_store


VALID_STATES = {"ativo", "concluído", "comprometido"}
TERMINAL_STATES = {"concluído", "comprometido"}


class BatchStateError(ValueError):
    status_code = 400


class BatchCalculationError(ValueError):
    status_code = 400


class BatchNotFoundError(ValueError):
    status_code = 404


class BatchValidationError(ValueError):
    status_code = 400


def validate_batch(payload):
    """Validate batch creation payload."""
    if payload is None or not isinstance(payload, dict):
        raise BatchValidationError("Payload must be a JSON object.")

    if payload.get("herb_id") is None:
        raise BatchValidationError("herb_id is required.")

    planned_qty = payload.get("planned_qty")
    if planned_qty is None:
        raise BatchValidationError("planned_qty is required.")
    if not isinstance(planned_qty, (int, float)) or isinstance(planned_qty, bool):
        raise BatchValidationError("planned_qty must be a number.")
    if planned_qty <= 0:
        raise BatchValidationError("planned_qty must be > 0.")


def transition_batch_state(current_state, has_losses, end_date_set):
    if current_state not in VALID_STATES:
        raise BatchStateError(f"Estado inválido: '{current_state}'.")
    if current_state in TERMINAL_STATES:
        raise BatchStateError(
            f"Lote já está em estado terminal '{current_state}'; transição não permitida."
        )
    if not end_date_set:
        raise BatchStateError("Data de conclusão obrigatória para fechar o lote.")
    return "comprometido" if has_losses else "concluído"


def calculate_productivity(planned_qty, actual_qty, losses):
    if not isinstance(planned_qty, (int, float)) or isinstance(planned_qty, bool):
        raise BatchCalculationError("planned_qty must be a number.")
    if not isinstance(actual_qty, (int, float)) or isinstance(actual_qty, bool):
        raise BatchCalculationError("actual_qty must be a number.")
    if not isinstance(losses, (int, float)) or isinstance(losses, bool):
        raise BatchCalculationError("losses must be a number.")
    if planned_qty <= 0:
        raise BatchCalculationError("planned_qty must be > 0.")
    if actual_qty < 0:
        raise BatchCalculationError("actual_qty must be >= 0.")
    if losses < 0:
        raise BatchCalculationError("losses must be >= 0.")
    if losses > actual_qty:
        raise BatchCalculationError("losses cannot exceed actual_qty.")
    return round((actual_qty - losses) / planned_qty * 100, 2)


def list_batches():
    return memory_store.list_batches()


def create_batch(payload):
    validate_batch(payload)
    return memory_store.add_batch({
        "herb_id":      payload["herb_id"],
        "plan_id":      payload.get("plan_id"),
        "state":        "ativo",
        "planned_qty":  payload["planned_qty"],
        "actual_qty":   None,
        "losses":       None,
        "productivity": None,
    })


def close_batch(batch_id, has_losses, actual_qty, losses):
    batch = memory_store.find_batch_by_id(batch_id)
    if batch is None:
        raise BatchNotFoundError(f"Lote {batch_id} não encontrado.")
    new_state = transition_batch_state(batch["state"], has_losses, end_date_set=True)
    productivity = calculate_productivity(batch["planned_qty"], actual_qty, losses)
    return memory_store.update_batch(batch_id, {
        "state": new_state, "actual_qty": actual_qty,
        "losses": losses, "productivity": productivity,
    })
