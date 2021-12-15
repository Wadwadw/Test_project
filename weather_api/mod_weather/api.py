from flask_restful import Api
from mod_weather.urls import Cities
from mod_weather.urls import Mean
from mod_weather.urls import MovingMean
from mod_weather.urls import Records

api = Api()

api.add_resource(Cities, '/cities')
api.add_resource(Mean, '/mean')
api.add_resource(Records, '/records')
api.add_resource(MovingMean, '/moving_mean')
