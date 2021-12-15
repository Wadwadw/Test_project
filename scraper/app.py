from flask import Flask
from flask_restful import Api
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{BASE_DIR}/weather_api/weather.db'
api = Api(app)

api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)