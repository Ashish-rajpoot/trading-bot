from __future__ import annotations

from app.models.order_request import OrderRequest
from app.models.trade import Trade


class OrderRequestBuilder:
    """
    Converts a Trade into an OrderRequest.
    """

    @staticmethod
    def build(trade: Trade) -> OrderRequest:
        """
        Build an OrderRequest from a Trade.
        """

        return OrderRequest(
            symbol=trade.symbol,
            side=trade.signal.name,
            size=trade.quantity,
            order_type="market",
            leverage=trade.leverage,
            price=None,
            stop_loss=trade.stop_loss,
            take_profit=trade.take_profit,
        )