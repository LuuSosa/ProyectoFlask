class Config(object):
    TESTING = False
    DEBUG=False
    SQLALCHEMY_DATABASE_URI ="mysql+pymysql://root:root@localhost:3306/tiendaa"


class ProductionConfig(Config):
    DEBUG = False
class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True