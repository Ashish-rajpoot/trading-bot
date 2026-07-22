from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class OrderResponse:
    """
    Represents the result of an order execution.
    """

    success: bool
    message: str

    order_id: int | None = None

    mode: str = "LIVE"