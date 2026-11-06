import pytest

from api.data import memory_store


@pytest.fixture(autouse=True)
def herbs_limpos():
    memory_store.reset_herbs()
    yield
    memory_store.reset_herbs()


_CSV_VALIDO = "name,family,description\nLavanda,Lamiaceae,Erva aromática\nMenta,Lamiaceae,Refrescante"
_CSV_VAZIO = ""


# ---------------------------------------------------------------------------
# TI-08 a TI-13 — GET /herbs e POST /herbs/import
# ---------------------------------------------------------------------------

def test_get_herbs_sem_token(client):
    """TI-08: GET /herbs sem token devolve 401."""
    r = client.get("/herbs")
    assert r.status_code == 401


def test_get_herbs_com_token(client, admin_h):
    """TI-09: GET /herbs com token válido devolve 200."""
    r = client.get("/herbs", headers=admin_h)
    assert r.status_code == 200
    assert "herbs" in r.json()


def test_import_herbs_sem_token(client):
    """TI-10: POST /herbs/import sem token devolve 401."""
    r = client.post("/herbs/import", content=_CSV_VALIDO,
                    headers={"Content-Type": "text/plain"})
    assert r.status_code == 401


def test_import_herbs_tecnico_proibido(client, tech_h):
    """TI-11: POST /herbs/import com perfil Técnico devolve 403."""
    r = client.post("/herbs/import", content=_CSV_VALIDO,
                    headers={**tech_h, "Content-Type": "text/plain"})
    assert r.status_code == 403


def test_import_herbs_admin_csv_valido(client, admin_h):
    """TI-12: POST /herbs/import com Admin e CSV válido devolve 200 com imported=2."""
    r = client.post("/herbs/import", content=_CSV_VALIDO,
                    headers={**admin_h, "Content-Type": "text/plain"})
    assert r.status_code == 200
    assert r.json()["imported"] == 2


def test_import_herbs_admin_csv_vazio(client, admin_h):
    """TI-13: POST /herbs/import com CSV vazio devolve 400 ou 422."""
    r = client.post("/herbs/import", content=_CSV_VAZIO,
                    headers={**admin_h, "Content-Type": "text/plain"})
    assert r.status_code in (400, 422)
