#!/usr/bin/python
#coding: utf-8

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
location = geolocator.geocode("New York City")
print(location.address)
print((location.latitude, location.longitude))
