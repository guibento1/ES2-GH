from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from api.services.auth_service import TokenValidationError, decode_token

_bearer = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(_bearer),
):
    if not credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token em falta.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        return decode_token(credentials.credentials, expected_type="access")
    except TokenValidationError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc


def require_admin(user=Depends(get_current_user)):
    if user.get("role") != "Administrador":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Perfil Administrador requerido.",
        )
    return user


def require_responsavel_or_admin(user=Depends(get_current_user)):
    if user.get("role") not in ("Responsável Técnico", "Administrador"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Perfil Responsável Técnico ou Administrador requerido.",
        )
    return user
