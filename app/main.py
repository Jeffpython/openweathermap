from fastapi import FastAPI
import httpx


app = FastAPI()


def get_city_data(city: str, api_key: str) -> tuple[float, float]:
    response = httpx.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}')
    lat = response.json()[0]['lat']
    lon = response.json()[0]['lon']
    return lat, lon


def get_weather_data(lat: float, lon: float, api_key: str) -> dict:
    response = httpx.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=ru')
    return response.json()


@app.get('/weather/{city}')
def main(city: str) -> dict:
    api_key = 'ed03406521a9e4a91d46056b0aa6237c'
    lat, lon = get_city_data(city, api_key)
    weather_data = get_weather_data(lat, lon, api_key)
    return weather_data
