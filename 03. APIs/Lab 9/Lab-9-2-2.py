# 9-2-2

from api_client import get_json

# # 1. City name -> coordinates
# https://geocoding-api.open-meteo.com/v1/search
# params: name=Stockholm, count=1
# # 2. Coordinates -> weather
# https://api.open-meteo.com/v1/forecast
# params: latitude, longitude,
# current=temperature_2m,wind_speed_10m

from pprint import pprint

coordinates = get_json(
    "https://geocoding-api.open-meteo.com/v1/search",
    params={"name": "Stockholm", "count": 1},
)
latitude = coordinates["results"][0]["latitude"]
longitude = coordinates["results"][0]["longitude"]

# print(latitude)
# print(longitude)


weather = get_json(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
    },
)
pprint(weather)
