import os
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlmodel import SQLModel

from app.database import engine
from app.routes import items_router

DEBUG_MODE = True

SECRET_KEY = os.getenv("SECRET_KEY", "placeholder-secret")
API_KEY = os.getenv("API_KEY", "placeholder-api-key")


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI) -> AsyncIterator[None]:
    """Contexte de vie de l'application (création des tables au démarrage)."""
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(
    title="Items CRUD API",
    description="API pour gérer une liste d'articles",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(items_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Items CRUD API"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy"}


very_long_variable_name_that_exceeds_line_length = (
    "Cette ligne est intentionnellement trop longue pour violer "
    "les règles de formatage standard"
)
