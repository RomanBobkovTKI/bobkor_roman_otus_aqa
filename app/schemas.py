from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    name: str
    age: int
    job: str

    class Config:
        from_attributes = True