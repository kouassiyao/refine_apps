"""Bills API module."""

from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(tags=["bills"])


@router.post("/bills", response_model=Bill)
async def create_bill(bill: Bill, db: Session = Depends(get_db)):
    """
    Create a new bill.

    Args:
        bill (Bill): The bill to create.
        db (Session): The database session.

    Returns:
        Bill: The created bill.
    """
    try:
        db.add(bill)
        db.commit()
        db.refresh(bill)
        return bill
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))