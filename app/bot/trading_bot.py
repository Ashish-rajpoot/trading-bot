from __future__ import annotations

from app.exchange.market_data import MarketData
from app.indicators.ema_indicator import EMAIndicator
from app.models.signal import Signal
from app.risk.risk_manager import RiskManager
from app.services.order_service import OrderService
from app.strategies.ema_strategy import EMAStrategy

from datetime import UTC, datetime, timedelta

class TradingBot:
    """
    Main trading engine.
    """

    def __init__(
        self,
        market_data: MarketData,
        indicator: EMAIndicator,
        strategy: EMAStrategy,
        risk_manager: RiskManager,
        order_service: OrderService,
    ) -> None:

        self._market = market_data
        self._indicator = indicator
        self._strategy = strategy
        self._risk = risk_manager
        self._orders = order_service



    def run(self) -> None:

        end = datetime.now(UTC)

        start = end - timedelta(hours=2)

        candles = self._market.get_candles(
            symbol="BTCUSD",
            resolution="1m",
            start=int(start.timestamp()),
            end=int(end.timestamp()),
        )

        candles = self._indicator.calculate(candles)

        signal = self._strategy.generate_signal(candles)

        allowed, reason = self._risk.can_trade()

        print("=" * 70)
        print(f"Signal : {signal.value}")
        print(f"Risk   : {reason}")
        print("=" * 70)

        if not allowed:
            return

        if signal == Signal.HOLD:
            return

        print("Ready to place order...")