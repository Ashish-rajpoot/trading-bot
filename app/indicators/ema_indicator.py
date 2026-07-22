from __future__ import annotations

import pandas as pd

from app.indicators.base_indicator import BaseIndicator


class EMAIndicator(BaseIndicator):
    """
    Calculate Exponential Moving Averages.
    """

    def __init__(
        self,
        fast: int = 9,
        medium: int = 15,
        slow: int = 40,
    ) -> None:

        self.fast = fast
        self.medium = medium
        self.slow = slow

    def calculate(
        self,
        data: pd.DataFrame,
    ) -> pd.DataFrame:

        df = data.copy()

        df["ema_fast"] = (
            df["close"]
            .ewm(span=self.fast, adjust=False)
            .mean()
        )

        df["ema_medium"] = (
            df["close"]
            .ewm(span=self.medium, adjust=False)
            .mean()
        )

        df["ema_slow"] = (
            df["close"]
            .ewm(span=self.slow, adjust=False)
            .mean()
        )

        return df