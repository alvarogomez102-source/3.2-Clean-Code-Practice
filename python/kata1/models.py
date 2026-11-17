from dataclasses import dataclass


@dataclass(frozen=True)
class CafeItem:
    name: str
    price: float
    quantity: int


@dataclass(frozen=True)
class Sale:
    customer: str
    member: bool
    items: list[CafeItem]
