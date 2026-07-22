from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class OrderRequest:
    """
    Represents an order to be sent to the exchange.
    """

    symbol: str

    side: str

    size: float

    order_type: str

    leverage: int

    price: float | None = None

    stop_loss: float | None = None

    take_profit: float | None = None