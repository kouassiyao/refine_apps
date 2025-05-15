"""Vendor api schema for the transactions service."""

import uuid
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class VendorBase(BaseModel):
    """Base Vendor schema."""

    name: str
    vat_number: Optional[str] = None


class VendorCreate(VendorBase):
    """Schema for creating a new Vendor."""

    class Config:
        schema_extra = {
            "example": {
                "name": "Acme Corp",
                "vat_number": "VAT123456",
            }
        }


class VendorUpdate(VendorBase):
    """Schema for updating an existing Vendor."""

    name: Optional[str] = None
    vat_number: Optional[str] = None


class Vendor(VendorBase):
    """Schema for returning a Vendor."""

    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
