"""Database configuration."""

import os
from collections.abc import Generator

from sqlmodel import Session, create_engine

# 👉 Si DATABASE_URL n'est pas définie, on utilise SQLite dans un fichier local.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")

connect_args: dict[str, object] = {}
if DATABASE_URL.startswith("sqlite"):
    # Option nécessaire pour SQLite avec SQLAlchemy dans certains contextes
    connect_args = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, connect_args=connect_args)


def get_db() -> Generator[Session]:
    """Provide a database session."""
    with Session(engine) as session:
        yield session
