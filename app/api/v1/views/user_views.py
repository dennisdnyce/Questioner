from flask import Flask, request, jsonify, Blueprint
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

myusers = Blueprint('usr1', __name__, url_prefix='/api/v1')


from ..models.user_models import UserRegistration
from ..utils.validators import validate_users, validate_user_login

user = UserRegistration('firstname', 'lastname', 'othername', 'phoneNumber', 'username', 'email', 'password', 'confirm_password', 'isAdmin')
