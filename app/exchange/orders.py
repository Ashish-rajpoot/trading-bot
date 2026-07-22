from __future__ import annotations

from typing import Any

from app.api.client import DeltaRestClient


class Orders:

    def __init__(self, client: DeltaRestClient) -> None:
        self._client = client

    def place_order(
        self,
        product_id: int,
        size: float,
        side: str,
        order_type: str = "market_order",
    ) -> dict[str, Any]:

        payload = {
            "product_id": product_id,
            "size": size,
            "side": side,
            "order_type": order_type,
        }

        return self._client.post(
            endpoint="/v2/orders",
            body=payload,
            authenticated=True,
        )

    def cancel_order(
        self,
        order_id: int,
    ) -> dict[str, Any]:

        return self._client.delete(
            endpoint=f"/v2/orders/{order_id}",
            authenticated=True,
        )

    def get_order(
        self,
        order_id: int,
    ) -> dict[str, Any]:

        return self._client.get(
            endpoint=f"/v2/orders/{order_id}",
            authenticated=True,
        )

    def get_open_orders(self) -> dict[str, Any]:

        return self._client.get(
            endpoint="/v2/orders",
            authenticated=True,
        )

    def get_order_history(self) -> dict[str, Any]:

        return self._client.get(
            endpoint="/v2/orders/history",
            authenticated=True,
        )