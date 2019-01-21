from flask import Flask, jsonify
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)

from instance.config import app_config
from app.api.v1.views.user_views import myquestioner as usrv1
from app.api.v2.views.user_views import myquestionerv2 as usrv2
from app.api.v1.views.meetup_views import myquestioner as mtv1
from app.api.v2.views.meetup_views import myquestionerv2 as mtv2

def create_app(config):
    '''function creating the flask app'''
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'this-is-my-super-28294242-secret'
    jwt = JWTManager(app)
    app.register_blueprint(usrv1)
    app.register_blueprint(usrv2)
    app.register_blueprint(mtv1)
    app.register_blueprint(mtv2)
    app.config.from_object(app_config[config])
    return app
