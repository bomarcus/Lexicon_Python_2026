# 9-2-3

from api_client import get_json

# # 1. City name -> coordinates
# https://geocoding-api.open-meteo.com/v1/search
# params: name=Stockholm, count=1
# # 2. Coordinates -> weather
# https://api.open-meteo.com/v1/forecast
# params: latitude, longitude,
# current=temperature_2m,wind_speed_10m

from pprint import pprint

# coordinates = get_json(
#     "https://geocoding-api.open-meteo.com/v1/search",
#     params={"name": "Stockholm", "count": 1},
# )
# latitude = coordinates["results"][0]["latitude"]
# longitude = coordinates["results"][0]["longitude"]

# print(latitude)
# print(longitude)


# weather = get_json(
#     "https://api.open-meteo.com/v1/forecast",
#     params={
#         "latitude": latitude,
#         "longitude": longitude,
#         "current": "temperature_2m,wind_speed_10m",
#     },
# )
# pprint(weather)


def find_city(name):
    data = get_json(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": name, "count": 1},
    )
    if data is None:
        return None
    return data["results"][0]


def get_weather(latitude, longitude):
    data = get_json(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,wind_speed_10m",
        },
    )
    if data is None:
        return None
    return data["current"]


user_input = input("input city:")
city = find_city(user_input)
weather = get_weather(city["latitude"], city["longitude"])
print(
    f" {city['name']}, {city['country']}, has a temperature of {weather['temperature_2m']}°C, and a wind of {weather['wind_speed_10m']}km/h"
)
