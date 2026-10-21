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


# Server said no: 401
# Traceback (most recent call last):
#   File "/Users/mao/Documents/Github/LEXICON/Lexicon_Python_2026/03. APIs/Lab 9/Lab-9-3-5.py", line 24, in <module>
#     print(response.headers["X-RateLimit-Limit"])
#           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
#   File "/Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages/requests/structures.py", line 65, in __getitem__
#     return self._store[key.lower()][1]
#            ~~~~~~~~~~~^^^^^^^^^^^^^
# KeyError: 'x-ratelimit-limit'

## 401 Unauthorized
## 403 Forbidden
