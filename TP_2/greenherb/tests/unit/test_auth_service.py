from unittest.mock import patch

import pytest

from api.data import memory_store
from api.services.auth_service import (
    AuthInputValidationError,
    TokenValidationError,
    authenticate_user,
    decode_token,
    generate_token,
    refresh_token,
)
from tests.credentials import TEST_USERS


@pytest.fixture(autouse=True)
def clear_refresh_tokens():
    memory_store.REFRESH_TOKENS.clear()
    yield
    memory_store.REFRESH_TOKENS.clear()


def _admin_user():
    return authenticate_user("admin", TEST_USERS["admin"]["password"])


@pytest.mark.parametrize(
    "username, password, esperado",
    [
        ("admin", TEST_USERS["admin"]["password"], "ok"),
        ("admin", "errada", "401"),
        ("admin", "", "400"),
        ("admin", None, "400"),
        ("admin", "   ", "400"),
        ("admin", "a" * 1000, "400"),
        ("admin", TEST_USERS["admin"]["password"] + ";", "400"),
        ("errado", TEST_USERS["admin"]["password"], "401"),
        ("errado", "errada", "401"),
        ("", TEST_USERS["admin"]["password"], "400"),
        ("", "", "400"),
        (None, TEST_USERS["admin"]["password"], "400"),
        (None, None, "400"),
        ("   ", TEST_USERS["admin"]["password"], "400"),
        ("a" * 1000, TEST_USERS["admin"]["password"], "400"),
        ("@dm!n", TEST_USERS["admin"]["password"], "400"),
    ],
)
def test_authenticate_user(username, password, esperado):
    """Testa combinações de username/password; classe=PE; input=parametrizado; esperado=ok, 400 ou 401."""
    if esperado == "400":
        with pytest.raises(AuthInputValidationError):
            authenticate_user(username, password)
        return

    user = authenticate_user(username, password)

    if esperado == "ok":
        assert user is not None
        assert user["username"] == username
        assert "password" not in user
    else:
        assert user is None


@pytest.mark.parametrize(
    "user, token_type, esperado",
    [
        (_admin_user, "access", "ok"),
        (_admin_user, "refresh", "ok"),
        (lambda: None, "access", "erro"),
        (_admin_user, "invalido", "erro"),
    ],
)
def test_generate_token(user, token_type, esperado):
    """Testa emissão de tokens; classe=PE; input=user/tipo parametrizado; esperado=token ou erro."""
    resolved_user = user()

    if esperado == "erro":
        with pytest.raises(ValueError):
            generate_token(resolved_user, token_type=token_type)
        return

    token = generate_token(resolved_user, token_type=token_type)
    payload = decode_token(token, expected_type=token_type)

    assert len(token.split(".")) == 3
    assert payload["id"] == resolved_user["id"]
    assert payload["username"] == resolved_user["username"]
    assert payload["role"] == resolved_user["role"]
    assert payload["type"] == token_type
    assert "exp" in payload


@pytest.mark.parametrize(
    "token_factory, expected_type, esperado",
    [
        (lambda: generate_token(_admin_user(), token_type="access"), "access", "ok"),
        (lambda: generate_token(_admin_user(), token_type="access"), "refresh", "erro"),
        (lambda: "token-invalido", None, "erro"),
        (lambda: "", None, "erro"),
        (lambda: None, None, "erro"),
        (
            # Adultera 10 caracteres do meio da assinatura — garantidamente quebra o HMAC
            lambda: generate_token(_admin_user(), token_type="access")[:-10] + "AAAAAAAAAA",
            None,
            "erro",
        ),
        (
            lambda: _expired_access_token(),
            None,
            "erro",
        ),
    ],
)
def test_decode_token(token_factory, expected_type, esperado):
    """Testa validação de tokens; classe=PE; input=token parametrizado; esperado=payload ou erro."""
    token = token_factory()

    if esperado == "erro":
        with pytest.raises(TokenValidationError):
            decode_token(token, expected_type=expected_type)
        return

    payload = decode_token(token, expected_type=expected_type)

    assert payload["username"] == "admin"
    assert payload["role"] == "Administrador"
    assert payload["type"] == expected_type


@pytest.mark.parametrize(
    "refresh_factory, esperado",
    [
        (lambda: generate_token(_admin_user(), token_type="refresh"), "ok"),
        (lambda: _expired_refresh_token(), "erro"),
        (lambda: "refresh-invalido", "erro"),
        (lambda: "", "erro"),
        (lambda: None, "erro"),
        (lambda: _unregistered_refresh_token(), "401"),
    ],
)
def test_refresh_token(refresh_factory, esperado):
    """Testa renovação de tokens; classe=PE; input=refresh parametrizado; esperado=novo par, erro ou 401."""
    token = refresh_factory()

    if esperado == "erro":
        with pytest.raises(TokenValidationError):
            refresh_token(token)
        return

    token_pair = refresh_token(token)

    if esperado == "401":
        assert token_pair is None
    else:
        assert token_pair["token_type"] == "bearer"
        assert decode_token(token_pair["access_token"], expected_type="access")
        assert decode_token(token_pair["refresh_token"], expected_type="refresh")


def _expired_access_token():
    with patch("api.services.auth_service.ACCESS_TOKEN_EXPIRE_MINUTES", -1):
        return generate_token(_admin_user(), token_type="access")


def _expired_refresh_token():
    with patch("api.services.auth_service.REFRESH_TOKEN_EXPIRE_MINUTES", -1):
        return generate_token(_admin_user(), token_type="refresh")


def _unregistered_refresh_token():
    token = generate_token(_admin_user(), token_type="refresh")
    memory_store.REFRESH_TOKENS.clear()
    return token
