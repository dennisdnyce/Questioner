from flask import Flask, request, jsonify, Blueprint
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

myusers = Blueprint('usr1', __name__, url_prefix='/api/v1')


from ..models.user_models import UserRegistration
from ..utils.validators import validate_users, validate_user_login

user = UserRegistration('firstname', 'lastname', 'othername', 'phoneNumber', 'username', 'email', 'password', 'confirm_password', 'isAdmin')

@myusers.route('/auth/signup', methods=['POST'])
def register_user():
    ''' method to register a user on the application '''
    data = request.get_json()
    userId = len(user.All_Users) + 1
    firstname = data['firstname']
    lastname = data['lastname']
    othername = data['othername']
    phoneNumber = data['phoneNumber']
    username = data['username']
    usrs = user.get_username(username)
    if usrs in user.All_Users:
        return jsonify({"status": 409, "error": "Username already taken!"}), 409

    email = data['email']
    usr = user.get_user_email(email)
    if usr in user.All_Users:
        return jsonify({"status": 409, "error": "Email address already registered!"}), 409

    password = data['password']
    confirm_password = data['confirm_password']
    isAdmin = data['isAdmin']
    registered = user.registered
    user.register_a_user(userId, firstname, lastname, othername, phoneNumber, username, email,
                         generate_password_hash(password), generate_password_hash(confirm_password), registered, isAdmin
                        )
    user_validator = validate_users(data)

    if (user_validator != True):
        return user_validator

    return jsonify({"status": 201, "RegistrationMessage": "Registration Successful", "data": [{"Welcome": username, "Member Since": registered, "Member Id": userId}]}), 201

@myusers.route('/auth/login', methods=['POST'])
def login_user():
    ''' method to login a registered user '''
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    login_validator = validate_user_login(data)

    if (login_validator != True):
        return login_validator

    response = user.login_a_user(username, password)
    if not response:
        return jsonify({"status": 400, "data": [{"Message": "You have entered the wrong password or the wrong username!"}]}), 400
    return jsonify({"status": 200, "LoginMessage": "Login Successful", "data": [{"Welcome back": username}]}), 200

@myusers.route('/auth/users', methods=['GET'])
def get_all_registered_users():
    ''' method to get all the registered users '''
    return jsonify({"status": 200, "data": [{"All_Users": user.All_Users}]}), 200

@myusers.route('/auth/users/<int:userId>', methods=['GET'])
def get_registered_user(userId):
    ''' method to get a registered user '''
    data = request.get_json()
    username = data['username']
    theusername = user.get_username(username)
    email = data['email']
    themail = user.get_user_email(email)
    usr = user.get_a_user(userId)
    if usr in user.All_Users:
        myname = theusername and themail
        if myname:
            return jsonify({"status": 200, "FoundMessage": "User Found", "data": [{"Member Id": userId, "User": username, "User Email": email}]}), 200
    return jsonify({"status": 404, "UserMessage": "User not found!", "data": [{}]}), 404
