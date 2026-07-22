# app/api/endpoints.py
from .client import DeltaRestClient

class Endpoints:
    PRODUCTS = "/v2/products"
    WALLET = "/v2/wallet/balances"
    POSITIONS = "/v2/positions"
    ORDERS = "/v2/orders"

    def __init__(self, client: DeltaRestClient):
        self.client = client

    def get_products(self):
        return self.client.get("/v2/products")