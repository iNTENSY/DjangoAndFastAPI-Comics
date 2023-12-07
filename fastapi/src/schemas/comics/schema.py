from pydantic import BaseModel


class Comics(BaseModel):
    id: int
    title: str
    author: int
    rating: float

    class Config:
        orm_mode = True


class Ratings(BaseModel):
    comics_id: int
    user_id: int
    value: int

    class Config:
        orm_mode = True
