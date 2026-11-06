from api.services.mock_service import create_mock, list_mock


VALID_MODES = {"Manual", "Automático"}


class AutomationDecisionError(ValueError):
    status_code = 400


def decide_automation(mode, rule_active, measurement_recent):
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
