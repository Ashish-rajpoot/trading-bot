from __future__ import annotations

from typing import Any

from app.api.client import DeltaRestClient


class Products:
    """
    Client for Delta Exchange Products API.
    """

    def __init__(self, client: DeltaRestClient) -> None:
        self._client = client

    def get_products(self) -> dict[str, Any]:
        """
        Fetch all products.
        """
        return self._client.get("/v2/products")

    def get_product(self, product_id: int) -> dict[str, Any]:
        """
        Fetch a product by ID.
        """
        return self._client.get(f"/v2/products/{product_id}")

    def find_by_symbol(self, symbol: str) -> dict[str, Any] | None:
        """
        Find a product by its trading symbol.
        """
        response = self.get_products()

        for product in response["result"]:
            if product["symbol"] == symbol:
                return product

        return None

    def get_product_id(self, symbol: str) -> int:
        """
        Return the product ID for a trading symbol.
        """
        product = self.find_by_symbol(symbol)

        if product is None:
            raise ValueError(f"Product '{symbol}' not found.")

        return product["id"]