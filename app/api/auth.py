from __future__ import annotations

import hashlib
import hmac
import json
import time
from collections.abc import Mapping
from urllib.parse import urlencode

from app.config.settings import settings


class DeltaAuthenticator:
    """
    Creates authentication headers for Delta Exchange private REST APIs.
    """

    USER_AGENT = "delta-trader/1.0"

    def get_headers(
        self,
        method: str,
        endpoint: str,
        *,
        params: Mapping[str, object] | None = None,
        body: Mapping[str, object] | None = None,
    ) -> dict[str, str]:
        """
        Generate authentication headers for a private request.

        Parameters
        ----------
        method:
            HTTP method (GET, POST, PUT, DELETE)

        endpoint:
            API endpoint (e.g. /v2/orders)

        params:
            Query string parameters.

        body:
            JSON request body.
        """

        timestamp = str(int(time.time()))

        query_string = ""

        if params:
            query_string = "?" + urlencode(params)

        payload = ""

        if body:
            payload = json.dumps(
                body,
                separators=(",", ":"),
                sort_keys=True,
            )

        signature_data = (
            method.upper()
            + timestamp
            + endpoint
            + query_string
            + payload
        )

        signature = hmac.new(
            settings.api_secret.encode("utf-8"),
            signature_data.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()

        print("Signature Data:", repr(signature_data))
        print("Signature:", signature)


        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": self.USER_AGENT,
            "api-key": settings.api_key,
            "timestamp": timestamp,
            "signature": signature,
        }