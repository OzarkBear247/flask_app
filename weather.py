import forecastio
from geopy.geocoders import Nominatim
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_weather(address):
    api_key = os.environ['FORECASTIO_API_KEY']
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
    byDaily = forecastio.load_forecast(api_key, latitude, longitude).daily()
    summary = forecast.summary
    temperature = forecast.temperature
    for hourlyData in byDaily.data:
        return "Today will be {} with a High of {}°  and a Low of {}°  Humidity will be {} with a DewPoint of {}".format(forecast.summary, hourlyData.temperatureMax, hourlyData.temperatureMin, hourlyData.humidity, hourlyData.dewPoint)
       



