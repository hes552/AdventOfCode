# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 11:18:03 2021

@author: Smushy
"""

import requests
import json
from pprint import pprint
x = {}
# API KEY
API_key = "4a2927d997acae252118c1b31d3f72ed"
 
# This stores the url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
# This will ask the user to enter city ID
city_name = input("which cities weather? :")
 
# This is final url. This is concatenation of base_url, API_key and city_id
Final_url = base_url + "q=" + city_name + "&appid=" + API_key 
 
# this variable contain the JSON data which the API returns
weather_data = requests.get(Final_url).json()
 
print("The current temperature is",(weather_data["main"]["temp"]-273),"celcius")
pprint(weather_data)
# JSON data is difficult to visualize, so you need to pretty print 


