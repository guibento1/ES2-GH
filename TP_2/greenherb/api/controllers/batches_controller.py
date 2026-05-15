from fastapi import HTTPException, status

from api.services.batch_service import (
    BatchCalculationError,
    BatchNotFoundError,
    BatchStateError,
    close_batch,
    create_batch,
    list_batches,
)


def get_batches():
    return {"batches": list_batches()}


def post_batch(payload: dict):
    return create_batch(payload)


def patch_close_batch(batch_id: int, payload: dict):
    try:
        return close_batch(
            batch_id=batch_id,
            has_losses=payload["has_losses"],
            actual_qty=payload["actual_qty"],
            losses=payload.get("losses", 0.0),
        )
    except BatchNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    except (BatchStateError, BatchCalculationError) as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
