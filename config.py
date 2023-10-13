class Config(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    SECRET_KEY = 'you-will-never-guess'
    JWT_SECRET_KEY = 'jwt-secret-string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASIC_AUTH_USERNAME = 'root'
    BASIC_AUTH_PASSWORD = 'root'
