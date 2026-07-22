from __future__ import annotations

from app.config.settings import Settings
from app.exchange.orders import Orders
from app.exchange.products import Products
from app.models.order_request import OrderRequest
from app.models.order_response import OrderResponse
from app.services.order_validator import OrderValidator

class OrderService:
    """
    Handles order execution.
    """

    def __init__(
        self,
        settings: Settings,
        orders: Orders,
        products: Products,
    ) -> None:
        self._settings = settings
        self._orders = orders
        self._products = products

    def execute(self, request: OrderRequest):
        """
        Execute an order in PAPER or LIVE mode.
        """
        OrderValidator.validate(request)
        
        if self._settings.trading_mode == "PAPER":
            return self._paper_trade(request)

        return self.place_market_order(request)

    def _paper_trade(
        self,
        request: OrderRequest,
    ) -> dict:

        return {
            "mode": "PAPER",
            "symbol": request.symbol,
            "side": request.side,
            "size": request.size,
            "status": "SIMULATED",
        }

    def place_market_order(
        self,
        request: OrderRequest,
    ) -> OrderResponse:

        product_id = self._products.get_product_id(
            request.symbol
        )

        return self._orders.place_order(
            product_id=product_id,
            side=request.side,
            size=request.size,
        )