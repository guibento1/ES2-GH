from fastapi import HTTPException, status

from api.services.alert_service import (
    AlertActionError,
    AlertNotFoundError,
    create_alert,
    list_alerts,
    resolve_alert,
)


def get_alerts():
    return {"alerts": list_alerts()}


def post_alert(payload: dict):
    return create_alert(payload)


def patch_alert(alert_id: int, payload: dict):
    try:
        return resolve_alert(
            alert_id=alert_id,
            action=payload["action"],
            justification=payload.get("justification"),
        )
    except AlertNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except AlertActionError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
