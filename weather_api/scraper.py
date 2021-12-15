import requests as r
from datetime import datetime as d
import datetime
import json
from mod_weather.endpoints import city_id

import sqlalchemy.exc

from mod_weather.models import Weather
from mod_weather.database import db

city_list = [['Kyiv', '50.45', '30.52'],
             ['Kharkiv', '49.98', '36.23'],
             ['Dnipro', '48.45', '34.98'],
             ['Lviv', '49.84', '24.03'],
             ['Ternopil', '49.55', '25.59']]
for city in city_list:
    lat = city[1]
    lon = city[2]

    response = r.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly&appid=6045b4cbdbb365cbfac7ac2c1b20b526&units=metric')
    data = json.loads(response.text)

    daily = data.get("daily")
    for day in daily:
        date_unix = day.get("dt")
        date = d.utcfromtimestamp(date_unix).strftime('%Y-%m-%d')
        clear_date = d.strptime(date, '%Y-%m-%d')
        temp = day.get("temp")
        temperature = temp.get("day")
        pcp = day.get("pop")
        clouds = day.get("clouds")
        pressure = day.get("pressure")
        humidity = day.get("humidity")
        wind_speed = day.get("wind_speed")
        id_city = json.loads(city_id(name=city[0]))
        weather = Weather(
            date=clear_date,
            city=id_city.get('id'),
            temp=temperature,
            pcp=pcp,
            clouds=clouds,
            pressure=pressure,
            humidity=humidity,
            wind_speed=wind_speed,
        )
        db.session.add(weather)
        db.session.commit()