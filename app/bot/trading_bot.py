from __future__ import annotations

import time

from app.models.order_request import OrderRequest
from app.models.signal import Signal

class TradingBot:
    """
    Main trading bot.
    """

    def __init__(
        self,
        settings,
        market_data,
        indicator,
        strategy,
        risk_manager,
        order_service,
    ) -> None:
        self._settings = settings
        self._market_data = market_data
        self._indicator = indicator
        self._strategy = strategy
        self._risk_manager = risk_manager
        self._order_service = order_service

    def run(self) -> None:

        end = int(time.time())
        start = end - (200 * 60)

        candles = self._market_data.get_candles(
            symbol=self._settings.symbol,
            resolution=self._settings.timeframe,
            start=start,
            end=end,
        )

        candles = self._indicator.calculate(candles)

        signal = self._strategy.generate_signal(candles)

        print("=" * 70)
        print(f"Symbol     : {self._settings.symbol}")
        print(f"Timeframe  : {self._settings.timeframe}")
        print(f"Signal     : {signal.name}")

        if not self._risk_manager.can_trade():

            print("Risk       : Trading blocked.")
            return

        print("Risk       : Trading allowed.")
        print("=" * 70)

        if signal is Signal.HOLD:
            print("No trade opportunity.")
            return

        order = OrderRequest(
            symbol=self._settings.symbol,
            side=signal.name,
            size=1,
            order_type="market",
            leverage=1,
        )

        response = self._order_service.execute(order)

        print()
        print(response)