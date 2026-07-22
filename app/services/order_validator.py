from __future__ import annotations

from app.models.order_request import OrderRequest


class OrderValidator:
    """
    Validates an OrderRequest before execution.
    """

    VALID_SIDES = {"BUY", "SELL"}
    VALID_ORDER_TYPES = {"market", "limit"}

    @classmethod
    def validate(cls, request: OrderRequest) -> None:
        """
        Validate an order request.

        Raises
        ------
        ValueError
            If any field is invalid.
        """

        if not request.symbol.strip():
            raise ValueError("Symbol cannot be empty.")

        if request.side not in cls.VALID_SIDES:
            raise ValueError(
                f"Invalid side: {request.side}"
            )

        if request.size <= 0:
            raise ValueError(
                "Order size must be greater than zero."
            )

        if request.leverage < 1:
            raise ValueError(
                "Leverage must be at least 1."
            )

        if request.order_type.lower() not in cls.VALID_ORDER_TYPES:
            raise ValueError(
                f"Unsupported order type: {request.order_type}"
            )