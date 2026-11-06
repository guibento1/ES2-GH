import secrets


TEST_USERS = {
    "tecnico": {
        "password": secrets.token_urlsafe(24),
        "full_name": "Técnico de Estufa",
        "role": "Técnico",
    },
    "responsavel": {
        "password": secrets.token_urlsafe(24),
        "full_name": "Responsável Técnico",
        "role": "Responsável Técnico",
    },
    "admin": {
        "password": secrets.token_urlsafe(24),
        "full_name": "Administrador GREENHERB",
        "role": "Administrador",
    },
}
