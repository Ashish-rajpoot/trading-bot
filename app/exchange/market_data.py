from __future__ import annotations

from typing import Any

from app.api.client import DeltaRestClient

import pandas as pd

class MarketData:
    """
    Client for Delta Exchange Market Data API.
    """

    def __init__(self, client: DeltaRestClient) -> None:
        self._client = client

    def get_ticker(self, symbol: str) -> dict[str, Any]:
        """
        Get ticker for a trading symbol.
        """
        return self._client.get(
            endpoint="/v2/tickers",
            params={
                "symbol": symbol,
            },
        )

    def get_orderbook(
        self,
        symbol: str,
    ) -> dict[str, Any]:
        """
        Get order book.
        """
        return self._client.get(
            endpoint="/v2/l2orderbook",
            params={
                "symbol": symbol,
            },
        )

    def get_candles(
            self,
            symbol: str,
            resolution: str,
            start: int,
            end: int,
        ) -> pd.DataFrame:

            response = self._client.get(
                endpoint="/v2/history/candles",
                params={
                    "symbol": symbol,
                    "resolution": resolution,
                    "start": start,
                    "end": end,
                },
            )

            df = pd.DataFrame(response["result"])

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

            df[numeric_columns] = df[numeric_columns].astype(float)

            df = df.sort_values("time").reset_index(drop=True)

            return df