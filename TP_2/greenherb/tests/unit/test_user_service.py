import pytest

from api.services.user_service import UserValidationError, validate_user


# ---------------------------------------------------------------------------
# TU-133 a TU-137 — PE: perfil de utilizador (role)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, role, esperado",
    [
        ("TU-133", "Técnico",             "ok"),    # PE: perfil válido
        ("TU-134", "Responsável Técnico", "ok"),    # PE: perfil válido
        ("TU-135", "Administrador",       "ok"),    # PE: perfil válido
        ("TU-136", "Gestor",              "erro"),  # PE: perfil inválido
        ("TU-137", None,                  "erro"),  # PE: perfil ausente
    ],
)
def test_user_role(test_id, role, esperado):
    """PE: validate_user — perfis válidos (Técnico, Responsável Técnico, Administrador) e inválido (TU-133 a TU-137)."""
    payload = {"username": "utilizador", "password": "pass123", "role": role}
    if esperado == "erro":
        with pytest.raises(UserValidationError):
            validate_user(payload)
    else:
        validate_user(payload)


# ---------------------------------------------------------------------------
# TU-138 a TU-142 — PE: campos obrigatórios
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "test_id, payload, esperado",
    [
        ("TU-138", {"username": "u", "password": "p", "role": "Técnico"}, "ok"),    # PE: payload válido completo
        ("TU-139", {"password": "p", "role": "Técnico"},                  "erro"),  # PE: username em falta
        ("TU-140", {"username": "u", "role": "Técnico"},                  "erro"),  # PE: password em falta
        ("TU-141", {"username": "u", "password": "p"},                    "erro"),  # PE: role em falta
        ("TU-142", {"username": "", "password": "p", "role": "Técnico"},  "erro"),  # PE: username vazio
    ],
)
def test_user_campos_obrigatorios(test_id, payload, esperado):
    """PE: validate_user — campos obrigatórios presentes e não vazios (TU-138 a TU-142)."""
    if esperado == "erro":
        with pytest.raises(UserValidationError):
            validate_user(payload)
    else:
        validate_user(payload)
