from flask import Flask

from instance.config import app_config
from .api.v1.views.user_views import myusers as usrv1
from .api.v1.views.meetup_views import mymeets as meetv1

def create_app(config):
    '''function creating the flask app'''
    app = Flask(__name__)
    app.register_blueprint(usrv1)
    app.register_blueprint(meetv1)
    app.config.from_object(app_config[config])
    return app
