from fastapi import APIRouter, Depends, status

from api.controllers import audit_controller
from api.dependencies.auth_deps import require_admin

router = APIRouter(prefix="/audit", tags=["audit"])

@router.get("", status_code=status.HTTP_200_OK)
def get_audit_logs(user=Depends(require_admin)):
    return audit_controller.get_audit_logs()
