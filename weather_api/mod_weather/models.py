from flask_sqlalchemy import SQLAlchemy
from mod_weather.database import db
from mod_weather.serializers import Serializer



class City(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)

    def serialize(self):
        data = Serializer.serialize(self)
        return data


class Weather(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.ForeignKey("city.id"))
    date = db.Column(db.Date)
    temp = db.Column(db.Integer)
    pcp = db.Column(db.Integer)
    clouds = db.Column(db.Integer)
    pressure = db.Column(db.Integer)
    humidity = db.Column(db.Integer)
    wind_speed = db.Column(db.Integer)

    def serialize(self):
        data = Serializer.serialize(self)
        return data