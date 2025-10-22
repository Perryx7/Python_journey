"""
pip is for manage package in python 
pip requests
pip list == list all the package you have installed
pip install requests== 2.30.0 install the specific version of your package

env = virtaul environnement
how to provide two modules of the same module? virtaul environnement is the solution
to create a virtaul env:
py -m venv .venv
activate your venv :
source .venv/Scripts/activate
to deactivate : just type deactivate

"""

"""weather"""

import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_curr_weather():
    print("\n**** GET CURRENT WEATHER CONDITIONS ****")

    city = input("\nPlease enter a city name: ")

    api_key = os.getenv("API_KEY")  # store API key in a variable
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=imperial"

    # Fetch weather data
    weather_data = requests.get(request_url).json()

    # Display results safely
    if weather_data.get("cod") != 200:
        print(f"❌ Error: {weather_data.get('message')}")
        return

    print(f"\nCurrent weather for {weather_data['name']}")
    print(f"Temperature: {weather_data['main']['temp']}°F")
    print(f"Feels like: {weather_data['main']['feels_like']}°F")
    print(f"Conditions: {weather_data['weather'][0]['description'].capitalize()}")

    # pprint(weather_data)  # optional: full data

get_curr_weather()
