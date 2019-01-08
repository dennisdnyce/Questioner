from flask import Flask

from instance.config import app_config

def create_app(config):
    '''function creating the flask app'''
    app = Flask(__name__)
    app.config.from_object(app_config[config])
    return app
