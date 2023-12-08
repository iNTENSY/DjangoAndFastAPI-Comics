from pydantic import BaseModel


class Comics(BaseModel):
    id: int
    title: str
    author: int
    rating: float


class Ratings(BaseModel):
    comics_id: int
    user_id: int
    value: int
