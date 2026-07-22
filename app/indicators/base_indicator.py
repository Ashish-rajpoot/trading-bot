from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd


class BaseIndicator(ABC):
    """
    Base class for all technical indicators.
    """

    @abstractmethod
    def calculate(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate the indicator.

        Parameters
        ----------
        data : pd.DataFrame
            Market OHLCV data.

        Returns
        -------
        pd.DataFrame
            DataFrame with indicator columns.
        """
        raise NotImplementedError