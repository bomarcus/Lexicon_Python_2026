# 1

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


movies = [
    {
        "id": 1,
        "title": "The Shawshank Redemption",
        "director": "Frank Darabont",
        "year": 1994,
    },
    {"id": 2, "title": "Amour", "director": "Michael Haneke", "year": 2012},
    {
        "id": 3,
        "title": "Dallas Buyers Club",
        "director": "Jean Marc Vallée",
        "year": 2014,
    },
    {"id": 4, "title": "Persona", "director": "Ingmar Bergman", "year": 1966},
]


# return the movie list.
@app.get("/movies")
def list_movies(director: str | None = None, year: int | None = None):
    result = movies
    if director:
        result = [
            movie for movie in movies if director.lower() in movie["director"].lower()
        ]
    if year:
        result = [movie for movie in result if year == movie["year"]]
    return result


# 2
@app.get("/movies/{movie_id}")
def get_movies(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(
        status_code=404
    )  # gives 404 Undocumented Error: Not Found or For 'movie_id': Value must be an integer.
