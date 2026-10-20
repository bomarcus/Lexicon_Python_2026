# 9-2-1

from api_client import get_json

# # 1. City name -> coordinates
# https://geocoding-api.open-meteo.com/v1/search
# params: name=Stockholm, count=1
# # 2. Coordinates -> weather
# https://api.open-meteo.com/v1/forecast
# params: latitude, longitude,
# current=temperature_2m,wind_speed_10m

response = get_json(
    "https://geocoding-api.open-meteo.com/v1/search",
    params={"name": "Stockholm", "count": 1},
)

print(response["results"][0]["latitude"], response["results"][0]["longitude"])
