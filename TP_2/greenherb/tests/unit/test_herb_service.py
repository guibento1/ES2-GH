"""
Testes de unidade — Sprint 2
Módulo: api.services.herb_service  (TU-34 a TU-38)

TU-34  Catálogo vazio — importação de registos com campos opcionais vazios      PE
TU-35  Catálogo vazio — ficheiro CSV vazio gera erro                             PE
TU-36  Re-importação do mesmo catálogo duplica os registos já existentes         PE
TU-37  Importação de novas ervas não duplica as que já existiam no catálogo      PE
TU-38  Tipo de input errado (name inteiro em vez de string) gera erro            PE
"""

import pytest

from api.data import memory_store
from api.services.herb_service import (
    HerbValidationError,
    import_herbs_csv,
    validate_herb,
)


# ---------------------------------------------------------------------------
# Fixture: garante catálogo vazio antes e depois de cada teste
# ---------------------------------------------------------------------------

@pytest.fixture(autouse=True)
def catalogo_vazio():
    memory_store.reset_herbs()
    yield
    memory_store.reset_herbs()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _csv(*rows, header="name,family,description"):
    lines = [header] + [",".join(str(c) for c in r) for r in rows]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# TU-34 — Catálogo vazio + importar registos com campos opcionais vazios (PE)
# ---------------------------------------------------------------------------

def test_tu34_importar_csv_catalogo_vazio():
    """PE: catálogo vazio aceita importação de CSV com campos opcionais em branco."""
    content = _csv(
        ["Manjericão", "", ""],
        ["Tomilho",    "", ""],
    )
    result = import_herbs_csv(content)

    assert result["imported"] == 2
    assert result["failed"] == 0
    assert len(memory_store.HERBS) == 2


# ---------------------------------------------------------------------------
# TU-35 — Catálogo vazio + ficheiro CSV vazio → erro (PE)
# ---------------------------------------------------------------------------

def test_tu35_csv_vazio_gera_erro():
    """PE: importar ficheiro vazio lança HerbValidationError."""
    with pytest.raises(HerbValidationError):
        import_herbs_csv("")


# ---------------------------------------------------------------------------
# TU-36 — Re-importação cria duplicados dos registos já existentes (PE)
# ---------------------------------------------------------------------------

def test_tu36_reimportacao_duplica_existentes():
    """PE: reimportar as mesmas ervas acrescenta duplicados ao catálogo."""
    # Importação inicial: 2 ervas
    import_herbs_csv(_csv(["Manjericão", "Lamiaceae", ""], ["Tomilho", "Lamiaceae", ""]))
    assert len(memory_store.HERBS) == 2

    # Re-importação das mesmas 2 + 1 nova
    result = import_herbs_csv(_csv(
        ["Manjericão", "Lamiaceae", ""],
        ["Tomilho",    "Lamiaceae", ""],
        ["Orégão",     "Lamiaceae", ""],
    ))

    assert result["imported"] == 3
    # catálogo tem agora 5 entradas: 2 originais + 3 reimportadas
    assert len(memory_store.HERBS) == 5
    nomes = [h["name"] for h in memory_store.HERBS]
    assert nomes.count("Manjericão") == 2
    assert nomes.count("Tomilho") == 2


# ---------------------------------------------------------------------------
# TU-37 — Importar ervas novas não duplica as já existentes (PE)
# ---------------------------------------------------------------------------

def test_tu37_importar_novas_nao_duplica_existentes():
    """PE: importar ervas com nomes distintos não afecta as já existentes."""
    # Estado inicial: 2 ervas
    import_herbs_csv(_csv(["Manjericão", "Lamiaceae", ""], ["Tomilho", "Lamiaceae", ""]))
    assert len(memory_store.HERBS) == 2

    # Importar apenas ervas novas
    result = import_herbs_csv(_csv(["Orégão", "Lamiaceae", ""], ["Menta", "Lamiaceae", ""]))

    assert result["imported"] == 2
    assert len(memory_store.HERBS) == 4
    nomes = [h["name"] for h in memory_store.HERBS]
    # Originais continuam com exactamente 1 ocorrência
    assert nomes.count("Manjericão") == 1
    assert nomes.count("Tomilho") == 1


# ---------------------------------------------------------------------------
# TU-38 — Tipo de input errado: name inteiro em vez de string (PE)
# ---------------------------------------------------------------------------

def test_tu38_tipo_input_errado_name_inteiro():
    """PE: name com tipo inteiro (em vez de string) lança HerbValidationError."""
    with pytest.raises(HerbValidationError):
        validate_herb({"name": 123})


# ---------------------------------------------------------------------------
# TU-80 — CSV misto: 1 linha válida + 1 linha inválida (PE)
# ---------------------------------------------------------------------------

def test_tu80_csv_misto_valida_e_invalida():
    """PE: importação de CSV com 1 linha válida e 1 inválida (name vazio) classifica corretamente."""
    content = _csv(
        ["Lavanda", "Lamiaceae", ""],
        ["",        "Lamiaceae", ""],
    )
    result = import_herbs_csv(content)

    assert result["imported"] == 1
    assert result["failed"] == 1
    assert len(memory_store.HERBS) == 1
    assert memory_store.HERBS[0]["name"] == "Lavanda"
