"""Bill business object model for the transactions service."""

import uuid
from sqlmodel import Field, Relationship, SQLModel
from app.models.vendors import Vendor
from app.models.common import TimestampMixin

class BomBill(SQLModel, TimestampMixin, table=True):
    """Base model for bills.""" 

    __tablename__ = "bills"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(description="Name of the bill")
    amount: float = Field(description="Amount of the bill")
    issue_date: str = Field(description="Date the bill was issued")
    due_date: str | None = Field(default=None, description="Due date of the bill")
    status: str

    vendor_id: uuid.UUID = Field(foreign_key="vendors.id")
    vendor: "Vendor" = Relationship()
