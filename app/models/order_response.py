from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class OrderResponse:
    """
    Result returned after placing an order.
    """

    success: bool

    order_id: int | None

    message: str