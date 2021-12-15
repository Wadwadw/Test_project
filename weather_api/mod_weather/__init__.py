from pathlib import Path

from flask import Flask
from mod_weather import settings
from mod_weather.api import api
from mod_weather.database import db


BASE_DIR = Path(__file__).resolve().parent.parent


app = Flask(__name__)
# app.config.from_object(settings.Config)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{BASE_DIR}/weather.db'
app.config['DEBUG'] = True
# from flask_sqlalchemy import SQLAlchemy
#
#
# db = SQLAlchemy(app)

db.init_app(app)

@app.route('/user/<username>', methods=['GET'])
def user_name(username):
    print(username)


api.init_app(app)
