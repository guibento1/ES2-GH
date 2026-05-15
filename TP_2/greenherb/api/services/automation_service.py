from api.services.mock_service import create_mock, list_mock


VALID_MODES = {"Manual", "Automático"}


class AutomationDecisionError(ValueError):
    """Raised when automation decision inputs are invalid."""
    status_code = 400


def decide_automation(mode, rule_active, measurement_recent):
    """
    Decide whether an automation action is executed, suggested, or ignored.

    Compound decision (MC/DC target):
        C1: mode == "Automático"
        C2: rule_active
        C3: measurement_recent

    Decision table:
        C2=F OR C3=F          → "ignorada"  (rule inactive or stale measurement)
        C1=T, C2=T, C3=T      → "executada" (automatic mode, all conditions met)
        C1=F, C2=T, C3=T      → "sugerida"  (manual mode, conditions met)

    Returns: "executada" | "sugerida" | "ignorada"
    Raises AutomationDecisionError for invalid inputs.
    """
    if mode not in VALID_MODES:
        raise AutomationDecisionError(
            f"mode must be one of: {', '.join(sorted(VALID_MODES))}."
        )
    if not isinstance(rule_active, bool):
        raise AutomationDecisionError("rule_active must be a boolean.")
    if not isinstance(measurement_recent, bool):
        raise AutomationDecisionError("measurement_recent must be a boolean.")

    if not rule_active or not measurement_recent:
        return "ignorada"

    return "executada" if mode == "Automático" else "sugerida"


def list_automation_rules():
    return list_mock("automation")


def create_automation_rule(payload):
    return create_mock("automation", payload)
