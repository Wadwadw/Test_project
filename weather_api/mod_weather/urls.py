from flask import request
from flask_restful import Resource
from mod_weather.endpoints import cities
from mod_weather.endpoints import mean
from mod_weather.endpoints import moving_mean
from mod_weather.endpoints import records


class Cities(Resource):
    @staticmethod
    def get():
        return cities()


class Mean(Resource):
    @staticmethod
    def get():
        value_type = request.args.get('value_type')
        city = request.args.get('city')
        return mean(value_type=value_type, city=city)


class Records(Resource):
    @staticmethod
    def get():
        city = request.args.get('city')
        start_dt = request.args.get('start_dt')
        end_dt = request.args.get('end_dt')
        return records(city=city, start_dt=start_dt, end_dt=end_dt)


class MovingMean(Resource):
    @staticmethod
    def get():
        value_type = request.args.get('value_type')
        city = request.args.get('city')
        return moving_mean(value_type=value_type, city=city)
