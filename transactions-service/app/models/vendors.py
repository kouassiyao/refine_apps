"""Vendor model for the transactions service."""

import uuid
from sqlmodel import Field, SQLModel

class VendorBase(SQLModel, table=True):
    """Base model for vendors."""

    __tablename__ = "vendors"

    name: str
    category: str
    created_at: str | None = Field(default=None)
    updated_at: str | None = Field(default=None)

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "name": "Vendor Name",
    #             "category": "Category Name",
    #             "created_at": "2023-10-01T12:00:00Z",
    #             "updated_at": "2023-10-01T12:00:00Z"
    #         }
    #     }


class Vendor(VendorBase, table=True):
    """Vendor full model"""

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "vendor_id": "12345",
    #             "name": "Vendor Name",
    #             "category": "Category Name",
    #             "created_at": "2023-10-01T12:00:00Z",
    #             "updated_at": "2023-10-01T12:00:00Z"
    #         }
    #     }
