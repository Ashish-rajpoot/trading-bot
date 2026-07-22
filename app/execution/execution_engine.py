from __future__ import annotations

from app.models.trade import Trade
from app.services.order_service import OrderService
from app.services.trade_journal import TradeJournal


class ExecutionEngine:
    """
    Executes trades and records them.
    """

    def __init__(
        self,
        order_service: OrderService,
        trade_journal: TradeJournal,
    ) -> None:
        self._order_service = order_service
        self._trade_journal = trade_journal

    def execute(self, trade: Trade):

        response = self._order_service.execute(trade)

        if response.success:

            if trade.trading_mode == "PAPER":
                trade.mark_simulated()
            else:
                trade.mark_filled(response.order_id)

        else:
            trade.mark_rejected()

        self._trade_journal.log(trade)

        return response