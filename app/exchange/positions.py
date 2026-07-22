from __future__ import annotations

from app.api.client import DeltaRestClient


class Positions:
    """
    Handles open position retrieval.
    """

    def __init__(self, client: DeltaRestClient) -> None:
        self._client = client

    def get_positions(self) -> list[dict]:
        """
        Return all open positions.
        """
        response = self._client.get(
            endpoint="/v2/positions"
        )

        return response.get("result", [])

    def has_open_position(
        self,
        symbol: str,
    ) -> bool:
        """
        Return True if an open position exists.
        """

        positions = self.get_positions()

        for position in positions:

            if (
                position.get("product_symbol") == symbol
                and float(position.get("size", 0)) != 0
            ):
                return True

        return False

    def get_position(
        self,
        symbol: str,
    ) -> dict | None:

        positions = self.get_positions()

        for position in positions:

            if (
                position.get("product_symbol") == symbol
                and float(position.get("size", 0)) != 0
            ):
                return position

        return None