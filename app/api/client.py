from __future__ import annotations

from typing import Any

import requests

from app.api.auth import DeltaAuthenticator


class DeltaRestClient:
    """
    HTTP client for communicating with the Delta Exchange REST API.
    """

    DEFAULT_TIMEOUT = 10

    def __init__(self, base_url: str) -> None:
        self._base_url = base_url.rstrip("/")
        self._session = requests.Session()
        self._auth = DeltaAuthenticator()

    def _build_url(self, endpoint: str) -> str:
        """
        Build the complete URL.
        """
        return f"{self._base_url}/{endpoint.lstrip('/')}"

    def _request(
        self,
        method: str,
        endpoint: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        authenticated: bool = False,
    ) -> dict[str, Any]:
        """
        Send an HTTP request.
        """

        if authenticated:
            auth_headers = self._auth.get_headers(
                method=method,
                endpoint=endpoint,
                params=params,
                body=json,
            )

            headers = {
                **auth_headers,
                **(headers or {}),
            }

        response = self._session.request(
            method=method,
            url=self._build_url(endpoint),
            params=params,
            json=json,
            headers=headers,
            timeout=self.DEFAULT_TIMEOUT,
        )

        response.raise_for_status()

        return response.json()

    def get(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        authenticated: bool = False,
    ) -> dict[str, Any]:
        """
        Send a GET request.
        """
        return self._request(
            method="GET",
            endpoint=endpoint,
            params=params,
            headers=headers,
            authenticated=authenticated,
        )

    def post(
        self,
        endpoint: str,
        json: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        authenticated: bool = False,
    ) -> dict[str, Any]:
        """
        Send a POST request.
        """
        return self._request(
            method="POST",
            endpoint=endpoint,
            json=json,
            headers=headers,
            authenticated=authenticated,
        )

    def put(
        self,
        endpoint: str,
        json: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        authenticated: bool = False,
    ) -> dict[str, Any]:
        """
        Send a PUT request.
        """
        return self._request(
            method="PUT",
            endpoint=endpoint,
            json=json,
            headers=headers,
            authenticated=authenticated,
        )

    def delete(
        self,
        endpoint: str,
        headers: dict[str, str] | None = None,
        authenticated: bool = False,
    ) -> dict[str, Any]:
        """
        Send a DELETE request.
        """
        return self._request(
            method="DELETE",
            endpoint=endpoint,
            headers=headers,
            authenticated=authenticated,
        )