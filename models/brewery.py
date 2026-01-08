from typing import Optional

from pydantic import BaseModel


class Brewery(BaseModel):
    id: str
    name: str
    brewery_type: str
    address_1: Optional[str] = None
    address_2: Optional[str] = None
    address_3: Optional[str] = None
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    phone: Optional[str] = None
    website_url: Optional[str] = None
    state: str
    street: Optional[str] = None
