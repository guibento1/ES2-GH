import csv
import io

from api.data import memory_store


MAX_NAME_LEN = 100
MAX_FAMILY_LEN = 100
MAX_DESCRIPTION_LEN = 500


class HerbValidationError(ValueError):
    """Raised when herb data is malformed or missing required fields."""
    status_code = 400


def _validate_herb_fields(name, family, description):
    """Validate individual herb fields; return list of error strings."""
    errors = []

    if name is None or (isinstance(name, str) and name.strip() == ""):
        errors.append("name is required")
    elif not isinstance(name, str):
        errors.append("name must be a string")
    elif len(name.strip()) > MAX_NAME_LEN:
        errors.append(f"name exceeds {MAX_NAME_LEN} characters")

    if family is not None and family != "":
        if not isinstance(family, str):
            errors.append("family must be a string")
        elif len(family.strip()) > MAX_FAMILY_LEN:
            errors.append(f"family exceeds {MAX_FAMILY_LEN} characters")

    if description is not None and description != "":
        if not isinstance(description, str):
            errors.append("description must be a string")
        elif len(description.strip()) > MAX_DESCRIPTION_LEN:
            errors.append(f"description exceeds {MAX_DESCRIPTION_LEN} characters")

    return errors


def validate_herb(payload):
    """Validate a herb creation payload dict; raises HerbValidationError on failure."""
    if payload is None or not isinstance(payload, dict):
        raise HerbValidationError("Payload must be a JSON object.")

    name = payload.get("name")
    family = payload.get("family")
    description = payload.get("description")

    errors = _validate_herb_fields(name, family, description)
    if errors:
        raise HerbValidationError("; ".join(errors))


def _classify_csv_row(row):
    """
    Classify a CSV row dict:
      - "valid":   name present and all fields within limits
      - "partial": name valid but at least one optional field invalid
      - "invalid": name missing, empty, or exceeds max length
    Returns (category, errors).
    """
    name = row.get("name", "").strip()
    family = row.get("family", "").strip()
    description = row.get("description", "").strip()

    name_errors = []
    optional_errors = []

    if name == "":
        name_errors.append("name is required")
    elif len(name) > MAX_NAME_LEN:
        name_errors.append(f"name exceeds {MAX_NAME_LEN} characters")

    if family and len(family) > MAX_FAMILY_LEN:
        optional_errors.append(f"family exceeds {MAX_FAMILY_LEN} characters")

    if description and len(description) > MAX_DESCRIPTION_LEN:
        optional_errors.append(f"description exceeds {MAX_DESCRIPTION_LEN} characters")

    if name_errors:
        return "invalid", name_errors + optional_errors
    if optional_errors:
        return "partial", optional_errors
    return "valid", []


def import_herbs_csv(content):
    """
    Parse CSV text and categorise each row as valid, partial, or invalid.
    Valid rows are persisted to the store.
    Raises HerbValidationError for an empty file or missing 'name' column.
    Returns a summary dict with counts and row details.
    """
    if not content or not content.strip():
        raise HerbValidationError("CSV content is empty.")

    reader = csv.DictReader(io.StringIO(content))

    if reader.fieldnames is None or "name" not in reader.fieldnames:
        raise HerbValidationError("CSV must contain a 'name' column.")

    valid_rows = []
    partial_rows = []
    invalid_rows = []

    for row in reader:
        category, errors = _classify_csv_row(row)
        if category == "valid":
            herb = memory_store.add_herb({
                "name": row["name"].strip(),
                "family": row.get("family", "").strip() or None,
                "description": row.get("description", "").strip() or None,
            })
            valid_rows.append(herb)
        elif category == "partial":
            partial_rows.append({"row": dict(row), "errors": errors})
        else:
            invalid_rows.append({"row": dict(row), "errors": errors})

    total = len(valid_rows) + len(partial_rows) + len(invalid_rows)
    if total == 0:
        raise HerbValidationError("CSV has no data rows.")

    return {
        "imported": len(valid_rows),
        "partial": len(partial_rows),
        "failed": len(invalid_rows),
        "valid": valid_rows,
        "partial_rows": partial_rows,
        "invalid": invalid_rows,
    }


def list_herbs():
    return memory_store.list_herbs()


def create_herb(payload):
    validate_herb(payload)
    return memory_store.add_herb({
        "name": payload["name"].strip(),
        "family": (payload.get("family") or "").strip() or None,
        "description": (payload.get("description") or "").strip() or None,
    })
