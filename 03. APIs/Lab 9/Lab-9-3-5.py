import os

import requests
from api_client import get_json
from dotenv import load_dotenv

load_dotenv(
    "/Users/mao/Documents/Github/LEXICON/Lexicon_Python_2026/03. APIs/Lab 9/9-3-1-2/.env"
)
token = os.getenv("GITHUB_TOKEN")

username_input = "bomarcus"

url = f"https://api.github.com/users/{username_input}/repos"
headers = {"Authorization": f"Bearer {token}"}

response = get_json(
    url,
    params={"sort": "pushed", "per_page": 5},
    headers=headers,
)

response = requests.get(url, headers=headers, timeout=5)
print(response.headers["X-RateLimit-Limit"])

response = requests.get(url, timeout=5)
print(response.headers["X-RateLimit-Limit"])
