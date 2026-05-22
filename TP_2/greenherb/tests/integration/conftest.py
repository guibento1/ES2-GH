import pytest
from fastapi.testclient import TestClient

from api.data import memory_store
from api.main import api
from api.services.auth_service import generate_token

_BATCH_SEED = [
    {
        "id": 1, "herb_id": 1, "plan_id": None,
        "state": "ativo", "planned_qty": 100.0,
        "actual_qty": None, "losses": None, "productivity": None,
    }
]


@pytest.fixture(scope="module")
def client():
    with TestClient(api) as c:
        yield c


def _token(username: str) -> str:
    user = memory_store.find_user_by_username(username)
    return generate_token(memory_store.public_user(user), token_type="access")


@pytest.fixture()
def admin_h():
    return {"Authorization": f"Bearer {_token('admin')}"}


@pytest.fixture()
def tech_h():
    return {"Authorization": f"Bearer {_token('tecnico')}"}


@pytest.fixture()
def resp_h():
    return {"Authorization": f"Bearer {_token('responsavel')}"}


@pytest.fixture(autouse=True)
def reset_store():
    memory_store.reset_plans()
    memory_store.reset_batches(seed=_BATCH_SEED)
    memory_store.reset_alerts()
    memory_store.reset_measurements()
    yield
    memory_store.reset_plans()
    memory_store.reset_batches()
    memory_store.reset_alerts()
    memory_store.reset_measurements()
