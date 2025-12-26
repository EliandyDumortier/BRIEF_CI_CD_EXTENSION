from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
import time

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
    start_time = time.time()
    try:
        result = ItemService.get_all(db, skip, limit)
        status_code = "200"
        return result
    finally:
        ITEMS_REQUEST_COUNT.labels(
            method="GET", endpoint="/items", status=status_code
        ).inc()
        ITEMS_REQUEST_LATENCY.labels(
            method="GET", endpoint="/items"
        ).observe(time.time() - start_time)


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(
    item_id: int,
    db: Session = Depends(get_db),
) -> Item:
    start_time = time.time()
    try:
        item = ItemService.get_by_id(db, item_id)
        if not item:
            status_code = "404"
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Item with id {item_id} not found",
            )
        status_code = "200"
        return item
    finally:
        ITEMS_REQUEST_COUNT.labels(
            method="GET", endpoint="/items/{id}", status=status_code
        ).inc()
        ITEMS_REQUEST_LATENCY.labels(
            method="GET", endpoint="/items/{id}"
        ).observe(time.time() - start_time)


@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(
    item_data: ItemCreate,
    db: Session = Depends(get_db),
) -> Item:
    start_time = time.time()
    try:
        item = ItemService.create(db, item_data)
        status_code = "201"
        return item
    finally:
        ITEMS_REQUEST_COUNT.labels(
            method="POST", endpoint="/items", status=status_code
        ).inc()
        ITEMS_REQUEST_LATENCY.labels(
            method="POST", endpoint="/items"
        ).observe(time.time() - start_time)


@router.put("/{item_id}", response_model=ItemResponse)
def update_item(
    item_id: int,
    item_data: ItemUpdate,
    db: Session = Depends(get_db),
) -> Item:
    start_time = time.time()
    try:
        item = ItemService.update(db, item_id, item_data)
        if not item:
            status_code = "404"
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Item with id {item_id} not found",
            )
        status_code = "200"
        return item
    finally:
        ITEMS_REQUEST_COUNT.labels(
            method="PUT", endpoint="/items/{id}", status=status_code
        ).inc()
        ITEMS_REQUEST_LATENCY.labels(
            method="PUT", endpoint="/items/{id}"
        ).observe(time.time() - start_time)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
) -> None:
    start_time = time.time()
    try:
        deleted = ItemService.delete(db, item_id)
        if not deleted:
            status_code = "404"
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Item with id {item_id} not found",
            )
        status_code = "204"
        return None
    finally:
        ITEMS_REQUEST_COUNT.labels(
            method="DELETE", endpoint="/items/{id}", status=status_code
        ).inc()
        ITEMS_REQUEST_LATENCY.labels(
            method="DELETE", endpoint="/items/{id}"
        ).observe(time.time() - start_time)
