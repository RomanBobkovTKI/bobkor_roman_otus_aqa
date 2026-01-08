from typing import List

from pydantic import BaseModel


class DogRandom(BaseModel):
    message: str
    status: str

class Dogs(BaseModel):
    message: List[str]
    status: str