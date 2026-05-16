from api.data import memory_store


VALID_ROLES = {"Técnico", "Responsável Técnico", "Administrador"}


class UserValidationError(ValueError):
    status_code = 400


def validate_user(payload):
    """Validate user creation payload."""
    if payload is None or not isinstance(payload, dict):
        raise UserValidationError("Payload must be a JSON object.")

    username = payload.get("username")
    if not username or not isinstance(username, str) or not username.strip():
        raise UserValidationError("username is required.")

    password = payload.get("password")
    if not password or not isinstance(password, str) or not password.strip():
        raise UserValidationError("password is required.")

    role = payload.get("role")
    if role is None:
        raise UserValidationError("role is required.")
    if role not in VALID_ROLES:
        raise UserValidationError(
            f"role must be one of: {', '.join(sorted(VALID_ROLES))}."
        )


def list_users():
    return [memory_store.public_user(user) for user in memory_store.USERS]
