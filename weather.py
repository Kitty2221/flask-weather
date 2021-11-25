import requests
from config import Config


def query_api(city):
    try:
        data = requests.get(
            Config.WEATHER_API_URL + "?key=" + Config.WEATHER_API_KEY + "&q=" + city + "&aqi=yes").json()
    except Exception as exc:
        print(exc)
        data = None
    return data
