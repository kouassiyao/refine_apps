"""Bill model for the transactions service."""

import uuid
from sqlmodel import Field, SQLModel

class BillBase(SQLModel, table=True):
    """Base model for bills."""
    __tablename__ = "bills"

    name: str
    amount: float
    due_date: str
    status: str
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)


class Bill(BillBase, table=True):
    """Bill full model"""

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
