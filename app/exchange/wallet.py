from __future__ import annotations

from typing import Any

from app.api.client import DeltaRestClient


class Wallet:
    """
    Wallet endpoints.
    """

    def __init__(
        self,
        client: DeltaRestClient,
    ) -> None:
        self._client = client

    def get_balances(self) -> dict[str, Any]:
        """
        Fetch account balances.
        """

        return self._client.get(
            endpoint="/v2/wallet/balances",
            authenticated=True,
        )