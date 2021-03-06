import os
'''Configuration files for the API'''

class Config(object):
    '''Parent configuration class'''
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET')
    DATABASE = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    '''configurations for development environment'''
    DEBUG = True
    TESTING = True

class StagingConfig(Config):
    '''configurations for staging environment'''
    DEBUG = True

class TestingConfig(Config):
    '''configurations for staging environment'''
    DEBUG = True
    TESTING = True
    TESTDATABASE = os.getenv('TESTDB')

class ProductionConfig(Config):
    '''configurations for production environment'''
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
}
