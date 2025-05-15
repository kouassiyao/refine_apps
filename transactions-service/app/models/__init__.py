"""Register models for the transactions service."""

__all__ = ["BomVendor", "BomBill"]

from .vendors import BomVendor
from .bills import BomBill
