"""Bill API interface definition."""

import uuid
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

    id: str
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True


    
