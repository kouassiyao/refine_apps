"""Database setup for the application."""

from typing import Generator
from sqlmodel import SQLModel, Session, create_engine

from app.core.config import settings
from app.models import BomBill, BomVendor

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI), echo=True)

def init_db() -> None:
    """Initialize the database.
    If using alembic migrations, this function is not needed.
    It is used to create the database tables if they do not exist.
    """
    # SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """Get a new session."""
    with Session(engine) as session:
        yield session
 