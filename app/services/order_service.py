from __future__ import annotations

from app.exchange.orders import Orders
from app.exchange.products import Products
from app.models.order_request import OrderRequest
from app.models.order_response import OrderResponse


class OrderService:
    """
    High-level service responsible for order execution.
    """

    def __init__(
        self,
        orders: Orders,
        products: Products,
    ) -> None:

        self._orders = orders
        self._products = products

    def place_market_order(
        self,
        request: OrderRequest,
    ) -> OrderResponse:

        product_id = self._products.get_product_id(
            request.symbol
        )

        response = self._orders.place_order(
            product_id=product_id,
            size=request.size,
            side=request.side,
            order_type=request.order_type,
        )

        if response.get("success"):

            return OrderResponse(
                success=True,
                order_id=response["result"]["id"],
                message="Order placed successfully.",
            )

        return OrderResponse(
            success=False,
            order_id=None,
            message=response.get("error", "Unknown error"),
        )