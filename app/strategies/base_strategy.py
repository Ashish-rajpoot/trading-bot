from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd

from app.models.signal import Signal


class BaseStrategy(ABC):
    """
    Base class for all trading strategies.
    """

    @abstractmethod
    def generate_signal(
        self,
        data: pd.DataFrame,
    ) -> Signal:
        """
        Generate a trading signal.
        """
        raise NotImplementedError