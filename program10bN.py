# -*- coding: utf-8 -*-
"""
Created on Fri May 26 14:44:32 2023

@author: HP
"""

import json

# Open the JSON file and read its contents
with open('weather.json', 'r') as f:
    data = f.read()

# Parse the JSON data into a Python dictionary
weather_dict = json.loads(data)

# Access the weather data from the dictionary
temperature = weather_dict['main']['temp']
humidity = weather_dict['main']['humidity']
description = weather_dict['weather'][0]['description']

# Print the weather data
print(f"Temperature: {temperature}°C")
print(f"Humidity: {humidity}%")
print(f"Description: {description}")