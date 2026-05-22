from fastapi import APIRouter, Depends, Query, status

from api.controllers import reports_controller
from api.dependencies.auth_deps import get_current_user

router = APIRouter(prefix="/reports", tags=["reports"])

@router.get("", status_code=status.HTTP_200_OK)
def get_reports(format: str = Query(default=None), user=Depends(get_current_user)):
    return reports_controller.get_reports(format)
