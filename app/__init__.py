from flask import Flask, jsonify
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

from instance.config import app_config
from app.api.v1.views.user_views import myquestioner as usrv1
from app.api.v2.views.user_views import myquestionerv2 as usrv2
from app.api.v1.views.meetup_views import myquestioner as mtv1
from app.api.v2.views.meetup_views import myquestionerv2 as mtv2

def page_not_found(e):
  return jsonify(
            {"error": "The url you are trying to access cannot be found. Please check your route and try again", "status": 404}
), 404

def method_not_found(e):
  return jsonify(
            {"error": "The http method you are using is not allowed for requested URL. Please check and try again", "status": 405}
), 405

def bad_request_method(e):
  return jsonify(
            {"error": "The server cannot understand the request you are asking of it. Please check and try again", "status": 400}
), 400

def internal_server_issues(e):
  return jsonify(
            {"error": "There was an internal server error, this could be anything; a typo error, a syntax error, or configuration issues", "status": 500}
), 500

def create_app(config):
    '''function creating the flask app'''
    app = Flask(__name__)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(405, method_not_found)
    app.register_error_handler(400, bad_request_method)
    app.register_error_handler(500, internal_server_issues)
    app.config['JWT_SECRET_KEY'] = 'this-is-my-super-28294242-secret'  # Change this!
    jwt = JWTManager(app)
    app.register_blueprint(usrv1)
    app.register_blueprint(usrv2)
    app.register_blueprint(mtv1)
    app.register_blueprint(mtv2)
    app.config.from_object(app_config[config])
    return app
