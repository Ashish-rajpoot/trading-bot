from __future__ import annotations

from datetime import datetime

import pandas as pd

from app.api.client import DeltaRestClient


class MarketData:
    """
    Handles historical market data retrieval.
    """

    def __init__(self, client: DeltaRestClient) -> None:
        self._client = client

    def get_candles(
        self,
        symbol: str,
        resolution: str,
        start: int,
        end: int,
    ) -> pd.DataFrame:
        """
        Fetch historical candle data.

        Returns
        -------
        pandas.DataFrame
            OHLCV dataframe sorted by time.
        """

        response = self._client.get(
            endpoint="/v2/history/candles",
            params={
                "symbol": symbol,
                "resolution": resolution,
                "start": start,
                "end": end,
            },
        )

        result = response.get("result")

        if not result:
            raise ValueError(
                f"No candle data returned for symbol '{symbol}'."
            )

        df = pd.DataFrame(result)

        required_columns = [
            "time",
            "open",
            "high",
            "low",
            "close",
            "volume",
        ]

        missing = [
            column
            for column in required_columns
            if column not in df.columns
        ]

        if missing:
            raise ValueError(
                f"Missing candle columns: {missing}"
            )

        df["time"] = pd.to_datetime(
            df["time"],
            unit="s",
            utc=True,
        )

        numeric_columns = [
            "open",
            "high",
            "low",
            "close",
            "volume",
        ]

        df[numeric_columns] = (
            df[numeric_columns]
            .apply(pd.to_numeric, errors="coerce")
        )

        df = df.dropna()

        df = (
            df.sort_values("time")
              .reset_index(drop=True)
        )

        return df

    def latest_candle(
        self,
        symbol: str,
        resolution: str,
        start: int,
        end: int,
    ) -> pd.Series:
        """
        Return the latest candle.
        """

        candles = self.get_candles(
            symbol=symbol,
            resolution=resolution,
            start=start,
            end=end,
        )

        return candles.iloc[-1]