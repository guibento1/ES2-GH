from api.services.mock_service import create_mock, list_mock


VALID_STATES = {"ativo", "concluído", "comprometido"}
TERMINAL_STATES = {"concluído", "comprometido"}


class BatchStateError(ValueError):
    """Raised when a batch state transition is invalid."""
    status_code = 400


class BatchCalculationError(ValueError):
    """Raised when productivity calculation inputs are invalid."""
    status_code = 400


def transition_batch_state(current_state, has_losses, end_date_set):
    """
    Determine the next batch state from the current state and conditions.

    Compound decision:
        C1: current_state == "ativo"   (only active batches can transition)
        C2: has_losses                 (losses present → comprometido)
        C3: end_date_set               (end date required to close)

    Transitions:
        C1=T, C3=T, C2=F → "concluído"
        C1=T, C3=T, C2=T → "comprometido"
        C1=T, C3=F        → BatchStateError (missing end date)
        C1=F              → BatchStateError (already in terminal state)

    Raises BatchStateError for invalid transitions.
    Returns the new state string.
    """
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
    """
    Calculate batch productivity as a percentage of the planned quantity.

        productivity = (actual_qty - losses) / planned_qty * 100

    Raises BatchCalculationError for invalid inputs:
        - planned_qty must be > 0
        - actual_qty must be >= 0
        - losses must be >= 0 and <= actual_qty
    """
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
    return list_mock("batches")


def create_batch(payload):
    return create_mock("batches", payload)
