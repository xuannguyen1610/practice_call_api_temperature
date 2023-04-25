from WeatherModel import Weather
from WeatherRepository import WeatherRepository
import requests
from fastapi import HTTPException


def get_weather_from_url(city: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=14655d11ad79eb31a185d40a301a7e06&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = Weather(
            city= city,
            temperature= data["main"]["temp"],
            description= data["weather"][0]["description"],
            humidity = data["main"]["humidity"]
    )
        return weather
    else:
        return None

def get_weather_from_db(city:str):
    weather_repo = WeatherRepository(host="157.230.244.233", user="stock_admin", password="aVBrVDczZzJ5OUVma3JR", database="stock")
    weather = weather_repo.select_weather_from_db(city)
    if weather is None:
        try:
            weather = get_weather_from_url(city)
            weather_repo.insert_weather_to_db(weather)
        except:
            weather = None
    return weather







