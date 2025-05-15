"""Timestamp mixin for SQLModel models."""

from typing import Optional
from datetime import datetime, timezone
from pydantic import BaseModel
from sqlmodel import Field


class TimestampMixin(BaseModel):
    """Mixin class to add created_at and updated_at timestamps to a model."""

    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    updated_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column_kwargs={
            "onupdate": lambda: datetime.now(timezone.utc)
        },
        nullable=False,
    )
