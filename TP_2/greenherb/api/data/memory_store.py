"""In-memory data used by the GREENHERB Sprint 1 API."""

from copy import deepcopy


USERS = [
    {
        "id": 1,
        "username": "tecnico",
        "password": "tecnico123",
        "full_name": "Técnico de Estufa",
        "role": "Técnico",
    },
    {
        "id": 2,
        "username": "responsavel",
        "password": "responsavel123",
        "full_name": "Responsável Técnico",
        "role": "Responsável Técnico",
    },
    {
        "id": 3,
        "username": "admin",
        "password": "admin123",
        "full_name": "Administrador GREENHERB",
        "role": "Administrador",
    },
]

REFRESH_TOKENS = {}


def find_user_by_username(username):
    """Return a copy of the user matching the supplied username."""
    for user in USERS:
        if user["username"] == username:
            return deepcopy(user)
    return None


def public_user(user):
    """Return user data without the password field."""
    if user is None:
        return None
    user_data = deepcopy(user)
    user_data.pop("password", None)
    return user_data
