from __future__ import annotations

import pandas as pd

from app.models.signal import Signal
from app.strategies.base_strategy import BaseStrategy


class EMAStrategy(BaseStrategy):
    """
    EMA 9 / 15 / 40 crossover strategy.
    """

    def generate_signal(
        self,
        data: pd.DataFrame,
    ) -> Signal:

        if len(data) < 2:
            return Signal.HOLD

        previous = data.iloc[-2]
        current = data.iloc[-1]

        # Bullish crossover
        if (
            previous["ema_fast"] <= previous["ema_medium"]
            and current["ema_fast"] > current["ema_medium"]
            and current["ema_medium"] > current["ema_slow"]
        ):
            return Signal.BUY

        # Bearish crossover
        if (
            previous["ema_fast"] >= previous["ema_medium"]
            and current["ema_fast"] < current["ema_medium"]
            and current["ema_medium"] < current["ema_slow"]
        ):
            return Signal.SELL

        return Signal.HOLD