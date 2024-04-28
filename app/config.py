class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    DEBUG = False
    