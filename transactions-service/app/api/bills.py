"""Bills API module."""

import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select
from app.core.db import get_session, Session

from app.schemas.bills import BillCreate, BillUpdate, Bill
from app.models.vendors import Vendor
from app.models.bills import BomBill

router = APIRouter(tags=["bills"])


@router.post("/bills", response_model=Bill)
async def create_bill(bill_create: BillCreate, db: Session = Depends(get_session)):
    """
    Create a new bill.
    Args:
        bill_create (BillCreate): The bill to create.
        db (Session): The database session.
    Returns:
        BillOutput: The created bill.
    Raises:
        HTTPException: If the bill could not be created.
    """

    # Check if the vendor exists
    vendor = db.exec(
        statement=select(Vendor).where(Vendor.id == bill_create.vendor_id)
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
