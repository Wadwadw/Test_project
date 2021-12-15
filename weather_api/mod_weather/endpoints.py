import json

from mod_weather.database import db
from mod_weather.models import City
from mod_weather.models import Weather
from sqlalchemy import and_
from sqlalchemy import func


def city_id(name: str) -> json:
    city = City.query.filter_by(name=name).first()
    return json.dumps(city.serialize())


def cities() -> list:
    city = City.query.all()
    data = City.serialize_list(city)
    list_of_cities = []
    for i in data:
        res = {
            'city_name': i.get('name')
        }
        list_of_cities.append(res)
    return list_of_cities


def mean(value_type: str, city: str) -> json:
    city_name = City.query.filter_by(name=city).first()
    city_id = city_name.serialize()
    id = city_id.get('id')
    weather = Weather.query.filter_by(city=id)
    avg_temp = Weather.query.with_entities(func.avg(getattr(Weather, value_type)).filter(Weather.city == id))

    return {
        'city': city,
        f'{value_type}': avg_temp[0][0],
    }


def records(city: str, start_dt: str, end_dt: str) -> json:
    city_name = City.query.filter_by(name=city).first()
    city_id = city_name.serialize()
    id = city_id.get('id')

    res = db.session.query(Weather).filter(and_(Weather.date <= end_dt, Weather.date >= start_dt, Weather.city == id))

    weather = Weather.serialize_list(res)

    return {
        'city': city,
        'start_dt': start_dt,
        'end_dt': end_dt,
        'weather': weather
    }


def moving_mean(value_type: str, city: str) -> json:
    city_name = City.query.filter_by(name=city).first()
    city_id = city_name.serialize()
    id = city_id.get('id')
    weather = Weather.query.filter_by(city=id)
    res = Weather.serialize_list(weather)

    list_date = []
    list_value = []
    n = 2
    N = 3
    final_res = {}

    for r in res:
        date = r.get('date')
        value = r.get(value_type)
        list_date.append(date)
        list_value.append(value)

    for i in range(len(list_value)-3):
        avg = (list_value[n-2] + list_value[n-1] + list_value[n])/N
        n += 1
        final_res[list_date[n]] = avg

    return {
        'city': city,
        f'{value_type}': final_res,
    }
