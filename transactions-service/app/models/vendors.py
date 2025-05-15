"""Vendor model for the transactions service."""

import uuid
from sqlmodel import Field, SQLModel
from app.models.common import TimestampMixin

class BomVendor(SQLModel, TimestampMixin, table=True):
    """Base model for vendors."""

    __tablename__ = "vendors"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(description="Name of the vendor")
    vat_number: str | None = Field(default=None)
