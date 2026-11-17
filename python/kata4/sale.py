from dataclasses import dataclass


@dataclass(frozen=True)
class Sale:
    product: str
    units: int
    unit_price: float
