import os
from dotenv import load_dotenv


load_dotenv()
class Config(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASIC_AUTH_USERNAME = os.environ.get('ADMIN_USERNAME')
    BASIC_AUTH_PASSWORD = os.environ.get('ADMIN_PASSWORD')
