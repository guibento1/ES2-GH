from fastapi import HTTPException, status

from api.services.automation_service import (
    AutomationDecisionError,
    create_automation_rule,
    decide_automation,
    list_automation_rules,
)


def get_automation_rules():
    return {"rules": list_automation_rules()}


def post_automation_rule(payload: dict):
    return create_automation_rule(payload)


def post_evaluate(payload: dict):
    try:
        decision = decide_automation(
            mode=payload["mode"],
            rule_active=payload["rule_active"],
            measurement_recent=payload["measurement_recent"],
        )
        return {"decision": decision}
    except AutomationDecisionError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
