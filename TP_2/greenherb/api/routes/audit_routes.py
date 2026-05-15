from fastapi import APIRouter, status

from api.controllers import audit_controller


router = APIRouter(prefix="/audit", tags=["audit"])


@router.get("", status_code=status.HTTP_200_OK)
def get_audit_logs():
    return audit_controller.get_audit_logs()
