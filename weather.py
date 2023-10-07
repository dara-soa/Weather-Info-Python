import requests
import json
from pprint import pprint

API_KEY = "49edcdeb737a08b5371c42f85fb4ce3d"

city = input("Enter a city: ")

final_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

weather_data = requests.get(final_url).json()

pprint(weather_data)