import os

import requests
from api_client import get_json
from dotenv import load_dotenv

BASE = "http://127.0.0.1:8000"
load_dotenv(
    "/Users/mao/Documents/Github/LEXICON/Lexicon_Python_2026/03. APIs/Lab 10/movies_api/.env"
)
key = os.getenv("API_KEY")

movies = get_json(f"{BASE}/movies")
print(movies)


new_movie = {"title": "Snow Crash", "director": "Neil Stevenson", "year": 1992}
response = requests.post(f"{BASE}/movies", json=new_movie, timeout=5)
print(response.status_code, response.json())


get_json(f"{BASE}/movies/99")
