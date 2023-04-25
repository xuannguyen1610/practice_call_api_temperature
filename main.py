from fastapi import FastAPI,HTTPException
from WeatherService import get_weather_from_db,get_weather_from_url



app = FastAPI()

@app.get("/weather/{city}")
async def get_weather(city:str):
    weather = get_weather_from_db(city)
    if weather is None:
        raise HTTPException(status_code=404, detail="CITY_NOT_FOUND")
    else:
        return weather.dict()


@app.put("/weather/{city}")
async def add_weather(city:str):
    weather = get_weather_from_url(city)
    if weather is None:
        raise HTTPException(status_code=404,detail="CITY_NOT_FOUND")
    else:
        return HTTPException(status_code=200,detail="{city} weather updated successfully")


