from __future__ import annotations

from app.api.client import DeltaRestClient


class Products:
    """
    Product service with in-memory caching.
    """

    def __init__(self, client: DeltaRestClient) -> None:
        self._client = client
        self._products: list[dict] | None = None

    def _load_products(self) -> list[dict]:
        """
        Load products once and cache them.
        """
        if self._products is None:
            response = self._client.get("/v2/products")
            self._products = response.get("result", [])

        return self._products

    def refresh(self) -> None:
        """
        Force refresh the product cache.
        """
        self._products = None
        self._load_products()

    def get_products(self) -> list[dict]:
        """
        Return all products.
        """
        return self._load_products()

    def get_product(self, product_id: int) -> dict | None:
        """
        Return a product by product ID.
        """
        for product in self._load_products():
            if product.get("id") == product_id:
                return product

        return None

    def find_by_symbol(self, symbol: str) -> dict | None:
        """
        Return a product by symbol.
        """
        for product in self._load_products():
            if product.get("symbol") == symbol:
                return product

        return None

    def get_product_id(self, symbol: str) -> int:
        """
        Return the product ID for a symbol.
        """
        product = self.find_by_symbol(symbol)

        if product is None:
            raise ValueError(f"Product '{symbol}' not found.")

        return product["id"]