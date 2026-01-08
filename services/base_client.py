import logging

import requests
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)


class BaseClient:
    def __init__(self, base_url: str, token: Optional[str] = None):
        self.base_url = base_url
        self.session = requests.Session()
        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})

    def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        logger.info(f"📤 {method.upper()} {url}")
        response = self.session.request(method=method, url=url, **kwargs)
        logger.info(f"📥 Response {response.status_code} from {url}")
        response.raise_for_status()
        return response

    def get(
        self, endpoint: str, params: Optional[Dict[str, Any]] = None
    ) -> requests.Response:
        return self._make_request("get", endpoint, params=params)

    def post(
        self, endpoint: str, json: Optional[Dict[str, Any]] = None
    ) -> requests.Response:
        return self._make_request("post", endpoint, json=json)
