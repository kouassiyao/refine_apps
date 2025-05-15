"""Bills API module."""

import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select
from app.core.db import get_session, Session

from app.schemas.bills import BillCreate, BillUpdate, Bill
from app.models.vendors import BomVendor
from app.models.bills import BomBill

router = APIRouter(tags=["bills"])


@router.post("/bills", response_model=Bill)
async def create_bill(bill_create: BillCreate, db: Session = Depends(get_session)):
    """Create a new bill."""

    # Check if the vendor exists
    vendor = db.exec(
        statement=select(BomVendor).where(BomVendor.id == bill_create.vendor_id)
    ).first()
    if not vendor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vendor not found",
        )

    # Create the bomBill object
    bom_bill = BomBill(
        **bill_create.model_dump(),
        id=uuid.uuid4(),
    )

    # Add the bill to the database
    try:
        db.add(bom_bill)
        db.commit()
        db.refresh(bom_bill)
        return bom_bill
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create bill",
        ) from e


@router.patch("/bills/{bill_id}", response_model=Bill)
async def update_bill(
    bill_id: uuid.UUID,
    bill_update: BillUpdate,
    db: Session = Depends(get_session),
):
    """Update a bill by ID."""
    bill = db.exec(
        select(BomBill).where(BomBill.id == bill_id)
    ).first()
    if not bill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bill not found",
        )

    # Update the bill
    for key, value in bill_update.model_dump(exclude_unset=True).items():
        setattr(bill, key, value)

    # Commit the changes to the database
    try:
        db.add(bill)
        db.commit()
        db.refresh(bill)
        return bill
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to update bill",
        ) from e
    

@router.get("/bills", response_model=list[Bill])
async def get_bills(db: Session = Depends(get_session)):
    """Get all bills."""
    bills = db.exec(select(BomBill)).all()
    return bills


@router.get("/bills/{bill_id}", response_model=Bill)
async def get_bill(bill_id: uuid.UUID, db: Session = Depends(get_session)):
    """Get a bill by ID."""
    bill = db.exec(
        select(BomBill).where(BomBill.id == bill_id)
    ).first()
    if not bill:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bill not found",
        )
    return bill