from flask_restful import Resource
from mod_weather.endpoints import cities, mean, records, moving_mean
from flask import request


class Cities(Resource):

    def get(self):
        return cities()


class Mean(Resource):

    def get(self):
        value_type = request.args.get('value_type')
        city = request.args.get('city')
        return mean(value_type=value_type, city=city)


class Records(Resource):

    def get(self):
        city = request.args.get('city')
        start_dt = request.args.get('start_dt')
        end_dt = request.args.get('end_dt')
        return records(city=city, start_dt=start_dt, end_dt=end_dt)


class MovingMean(Resource):

    def get(self):
        value_type = request.args.get('value_type')
        city = request.args.get('city')
        return moving_mean(value_type=value_type, city=city)
