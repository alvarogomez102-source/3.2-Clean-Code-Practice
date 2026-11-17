from dataclasses import dataclass


@dataclass(frozen=True)
class ShippingQuote:
    subtotal: float
    shipping: float
    total: float
