from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class OrderRequest:
    """
    Represents an order request that will be sent to the exchange.
    """

    symbol: str
    side: str
    size: float

    order_type: str = "market"
    leverage: int = 1

    price: float | None = None
    stop_loss: float | None = None
    take_profit: float | None = None