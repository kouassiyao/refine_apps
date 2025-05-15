"""Bill API interface definition."""

import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class BillBase(BaseModel):
    """Base Bill schema."""

    name: str
    amount: float
    issue_date: str
    due_date: Optional[str] = None
    status: str
    vendor_id: uuid.UUID


class BillCreate(BillBase):
    """Schema for creating a new Bill."""

    class Config:
        schema_extra = {
            "example": {
                "name": "Electricity Bill",
                "amount": 150.75,
                "issue_date": "2023-10-01",
                "due_date": "2023-10-15",
                "status": "unpaid",
                "vendor_id": uuid.uuid4(),
            }
        }


class BillUpdate(BillBase):
    """Schema for updating an existing Bill."""

    name: Optional[str] = None
    amount: Optional[float] = None
    issue_date: Optional[str] = None
    due_date: Optional[str] = None
    status: Optional[str] = None
    vendor_id: Optional[str] = None


class Bill(BillBase):
    """Schema for returning a Bill."""

    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
