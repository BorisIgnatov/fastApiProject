from pydantic import BaseModel


class Book(BaseModel):
    name: str
    author_id: int
    rating: int | None = 0


class Author(BaseModel):
    name: str


class Tag(BaseModel):
    name: str