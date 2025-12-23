from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.database import get_db
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate
from app.services.item_service import ItemService
from monitoring.metrics import (
    ITEMS_REQUEST_COUNT,
    ITEMS_REQUEST_LATENCY,
)

router = APIRouter(prefix="/items", tags=["items"])

MAX_ITEMS_PER_PAGE = 1000


@router.get("/", response_model=list[ItemResponse])
def get_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> list[Item]:
    with ITEMS_REQUEST_LATENCY.labels(endpoint="get_items").time():
        items = ItemService.get_all(db, skip, limit)

    ITEMS_REQUEST_COUNT.labels(
        method="GET",
        endpoint="/items",
        status="200",
    ).inc()

    return items


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(
    item_id: int,
    db: Session = Depends(get_db),
) -> Item:
    with ITEMS_REQUEST_LATENCY.labels(endpoint="get_item").time():
        item = ItemService.get_by_id(db, item_id)

    if not item:
        ITEMS_REQUEST_COUNT.labels(
            method="GET",
            endpoint="/items/{id}",
            status="404",
        ).inc()
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )

    ITEMS_REQUEST_COUNT.labels(
        method="GET",
        endpoint="/items/{id}",
        status="200",
    ).inc()

    return item


@router.post(
    "/",
    response_model=ItemResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_item(
    item_data: ItemCreate,
    db: Session = Depends(get_db),
) -> Item:
    with ITEMS_REQUEST_LATENCY.labels(endpoint="create_item").time():
        item = ItemService.create(db, item_data)

    ITEMS_REQUEST_COUNT.labels(
        method="POST",
        endpoint="/items",
        status="201",
    ).inc()

    return item


@router.put("/{item_id}", response_model=ItemResponse)
def update_item(
    item_id: int,
    item_data: ItemUpdate,
    db: Session = Depends(get_db),
) -> Item:
    with ITEMS_REQUEST_LATENCY.labels(endpoint="update_item").time():
        item = ItemService.update(db, item_id, item_data)

    if not item:
        ITEMS_REQUEST_COUNT.labels(
            method="PUT",
            endpoint="/items/{id}",
            status="404",
        ).inc()
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )

    ITEMS_REQUEST_COUNT.labels(
        method="PUT",
        endpoint="/items/{id}",
        status="200",
    ).inc()

    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
) -> None:
    deleted = ItemService.delete(db, item_id)

    if not deleted:
        ITEMS_REQUEST_COUNT.labels(
            method="DELETE",
            endpoint="/items/{id}",
            status="404",
        ).inc()
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found",
        )

    ITEMS_REQUEST_COUNT.labels(
        method="DELETE",
        endpoint="/items/{id}",
        status="204",
    ).inc()
