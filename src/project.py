# -*- coding: utf-8 -*-

from pprint import pprint
import requests
import csv
import json
import time
import sys
import calendar


## clave personal
APIKEY='5fcd9b38b58c67ae36a6d5451c03f5a2'

##coordenadas de el escorial (Madrid) 
latitud=40.5889
altitud=-4.1477



with open('C:/Users/kokea/Desktop/FILE.csv', mode='w', newline='') as weather_file:
    weather_writer = csv.writer(weather_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    weather_writer.writerow(['Place', 'Country', 'Weather', 'Weather_desc', 'Pressure', 'Humidity', 'Current_temp', 'Max_temp', 'Min_temp', 'Visibility', 'Wind_speed', 'Wind_degrees','Extract_EPOCH'])
    orig_time=calendar.timegm(time.gmtime())
    counter=3 #u
    while True:
        cont_time=calendar.timegm(time.gmtime())
        if cont_time-orig_time >=10:
            orig_time=cont_time
            counter=counter-1
            r = requests.get('http://api.openweathermap.org/data/2.5/weather?lat='+str(latitud)+'&lon='+str(altitud)+'&APPID='+str(APIKEY))
            data = r.json()
            print(data)
            Place = "'"+data['name']+"'"
            Country = "'"+data['sys']['country']+"'"
            Weather = "'"+data['weather'][0]['main']+"'"
            Weather_desc = "'"+data['weather'][0]['description']+"'"
            Pressure = data['main']['pressure']
            Humidity = data['main']['humidity']
            Current_temp = data['main']['temp']-273.15
            Max_temp = data['main']['temp_max']-273.15
            Min_temp = data['main']['temp_min']-273.15
            Visibility = data['visibility']
            Wind_speed = data['wind']['speed']
            Wind_degrees = data['wind']['deg']
            weather_writer.writerow([Place, Country, Weather, Weather_desc, str(Pressure), str(Humidity), str(Current_temp), str(Max_temp), str(Min_temp), str(Visibility), str(Wind_speed), str(Wind_degrees),str(cont_time)])
            
        if counter==0:
            break









