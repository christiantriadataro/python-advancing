from fastapi import FastAPI
from pydantic import BaseModel


class Review(BaseModel):
    num_stars: int
    text: str
    public: bool = False


class MovieReview(BaseModel):
    movie: str
    review: Review


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
