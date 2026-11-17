from dataclasses import dataclass


@dataclass(frozen=True)
class CartItem:
    name: str
    price: float
    quantity: int
