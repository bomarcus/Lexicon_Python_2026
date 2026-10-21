# ---- imports ----
import os

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel

# --- config ---
load_dotenv()
API_KEY = os.getenv("API_KEY")

# ---- app + data ----
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


# ---- models ----
class Movie(BaseModel):
    title: str
    director: str
    year: int


class MovieUpdate(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None


# ---- helpers ----
def find_movie(movie_id: int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="movie not found")


def check_key(x_api_key: str | None = Header(default=None)):
    if x_api_key != API_KEY or API_KEY is None:
        raise HTTPException(status_code=401)


# ---- routes: GET ----
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


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    return find_movie(movie_id)


# ---- routes: POST ----
@app.post("/movies", status_code=201, dependencies=[Depends(check_key)])
def create_movie(movie: Movie):
    new_id = max((m["id"] for m in movies), default=0) + 1
    new_movie = {
        "id": new_id,
        "title": movie.title,
        "director": movie.director,
        "year": movie.year,
    }
    movies.append(new_movie)
    return new_movie


# ---- routes: PUT ----
@app.put("/movies/{movie_id}", dependencies=[Depends(check_key)])
def replace_movie(movie_id: int, movie: Movie):
    existing = find_movie(movie_id)
    existing["title"] = movie.title
    existing["director"] = movie.director
    existing["year"] = movie.year
    return existing


# ---- routes: PATCH ----
@app.patch("/movies/{movie_id}", dependencies=[Depends(check_key)])
def patch_movie(movie_id: int, changes: MovieUpdate):
    existing = find_movie(movie_id)
    existing.update(changes.model_dump(exclude_unset=True))
    return existing


# ---- routes: DELETE ----
@app.delete("/movies/{movie_id}", status_code=204, dependencies=[Depends(check_key)])
def delete_movie(movie_id: int):
    existing = find_movie(movie_id)
    movies.remove(existing)


# 2.4
# PUT for updates to all fields in an entry
# PATCH for uptades to specific fields in an entry
