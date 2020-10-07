import calendar
from datetime import datetime

import requests


def get_weather(lat, lon, api_key):
    weather_response = requests.get(
        f"https://api.openweathermap.org/data/2.5/onecall?lat"
        f"={lat}&lon={lon}&exclude=hourly&appid={api_key}&"
        f"units=metric").json()
    return weather_response

def generate_weather_message(weather_response):
    current_weather = {
        "temperature": int(weather_response["current"]["temp"]),
        "day_of_week": calendar.day_name[datetime.fromtimestamp(
            weather_response["current"]["dt"]).weekday()],
        "description":
            weather_response["current"]["weather"][0]["description"],
        "main":
            weather_response["current"]["weather"][0]["main"]

    }