import calendar
from datetime import datetime

import requests


def get_weather(lat, lon, api_key):
    weather_response = requests.get(
        f"https://api.openweathermap.org/data/2.5/onecall?lat"
        f"={lat}&lon={lon}&exclude=hourly&appid={api_key}&"
        f"units=metric").json()
    return weather_response