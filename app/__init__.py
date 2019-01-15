from flask import Flask, jsonify

from instance.config import app_config
from app.api.v1.views.user_views import myquestioner as usrv1
from app.api.v1.views.meetup_views import myquestioner as mtv1

def create_app(config):
    '''function creating the flask app'''
    app = Flask(__name__)
    app.register_blueprint(usrv1)
    app.register_blueprint(mtv1)
    app.config.from_object(app_config[config])
    return app
