from pathlib import Path


class Config:
    BASE_DIR = Path(__file__).resolve().parent.parent
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASE_DIR}/weather.db'
