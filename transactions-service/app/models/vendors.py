"""Vendor model for the transactions service."""

import uuid
from sqlmodel import Field, SQLModel

class Vendor(SQLModel, table=True):
    """Base model for vendors."""

    __tablename__ = "vendors"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    vat_number: str | None = Field(default=None)
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)
