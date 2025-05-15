"""Vendors API module."""

import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select
from app.core.db import get_session, Session

from app.schemas.vendors import VendorCreate, VendorUpdate, Vendor
from app.models import BomVendor

router = APIRouter(tags=["vendors"])


@router.post("/vendors", response_model=Vendor)
async def create_vendor(vendor_create: VendorCreate, db: Session = Depends(get_session)):
    """
    Create a new vendor.
    """

    # Create the bomVendor object
    bom_vendor = BomVendor(
        **vendor_create.model_dump(),
        id=uuid.uuid4(),
    )

    # Add the vendor to the database
    try:
        db.add(bom_vendor)
        db.commit()
        db.refresh(bom_vendor)
        return bom_vendor
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create vendor",
        ) from e


@router.patch("/vendors/{vendor_id}", response_model=Vendor)
async def update_vendor(
    vendor_id: uuid.UUID,
    vendor_update: VendorUpdate,
    db: Session = Depends(get_session),
):
    """
    Update a vendor by ID.
    """
    vendor = db.exec(
        select(BomVendor).where(BomVendor.id == vendor_id)
    ).first()
    if not vendor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vendor not found",
        )

    # Update the vendor
    for key, value in vendor_update.model_dump(exclude_unset=True).items():
        setattr(vendor, key, value)

    db.add(vendor)
    db.commit()
    db.refresh(vendor)
    return vendor


@router.get("/vendors", response_model=list[Vendor])
async def get_vendors(db: Session = Depends(get_session)):
    """
    Get all vendors.
    """
    vendors = db.exec(select(BomVendor)).all()
    return vendors


@router.get("/vendors/{vendor_id}", response_model=Vendor)
async def get_vendor(vendor_id: uuid.UUID, db: Session = Depends(get_session)):
    """
    Get a vendor by ID.
    """
    vendor = db.exec(
        select(BomVendor).where(BomVendor.id == vendor_id)
    ).first()
    if not vendor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vendor not found",
        )
    return vendor
