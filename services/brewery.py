from typing import List

from models.brewery import Brewery
from services.base_client import BaseClient


class BreweryService(BaseClient):
    def get_brewery(self, brewery_id: str) -> Brewery:
        response = self.get(f"{brewery_id}")
        data = response.json()

        return Brewery(**data)

    def get_brewery_list(self) -> List[Brewery]:
        response = self.get("")
        data = response.json()

        return [Brewery(**brewery) for brewery in data]

    def get_brewery_by_name(self, name: str) -> List[Brewery]:
        response = self.get("", params={"name": name})
        data = response.json()

        return [Brewery(**brewery) for brewery in data]

    def get_brewery_by_random(self, size: int = None) -> List[Brewery]:
        response = self.get("random", params={"size": size})

        data = response.json()
        return [Brewery(**brewery) for brewery in data]