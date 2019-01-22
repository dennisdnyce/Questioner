import datetime

from flask import Flask, request, jsonify, Blueprint, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import psycopg2
from app.api.v2 import myquestionerv2
from ..models.user_models import UserRegistration
from ..utils.validators import validate_users, validate_user_login

myuser = UserRegistration()

@myquestionerv2.route('/auth/signup', methods=['POST'])
def register_user():
    ''' method to register a user on the application '''
    data = request.get_json()
    registered = myuser.registered
    isAdmin = myuser.isAdmin
    firstname = data['firstname']
    lastname = data['lastname']
    othername = data['othername']
    phoneNumber = data['phoneNumber']
    valid_phones = myuser.get_all_users()
    for valid_phone in valid_phones:
        if (phoneNumber == valid_phone):
                return jsonify({"status": 406, "error":"phone number already in use"}), 406
    username = data['username']
    email = data['email']
    password = data['password']
    confirm_password = data['confirm_password']

    user_validator = validate_users(data)

    if (user_validator != True):
        return user_validator
    access_token = create_access_token(identity=email)
    questioner_user = UserRegistration(firstname, lastname, othername, phoneNumber, username, email, generate_password_hash(password), generate_password_hash(confirm_password))

    questioner_user.register_a_user()

    return jsonify({"status": 201, "RegistrationMessage": "Registration Successful", "data": [{"Welcome": username, "token": access_token, "Member Since": registered}]}), 201

@myquestionerv2.route('/auth/login', methods=['POST'])
def login_a_user():
    ''' method to log in a user '''
    data = request.get_json()
    email = data['email']
    password = data['password']
    login_validator = validate_user_login(data)
    if (login_validator != True):
        return login_validator
    logger = myuser.login_a_user(email)
    if logger:
        data2 = request.get_json()
        found_password = data2['password']
        found_email = data2['email']
        if found_email:
            if check_password_hash(found_password, password):
                access_token = create_access_token(identity=user_email, expires_delta=datetime.timedelta(minutes=30))
                return jsonify({"Message": "User logged in successfully", "status": 200, "data": [{"token": access_token, "Welcome back": found_username}]}), 200
            return jsonify({"status": 404, "error": "Unable to login, check login credentials"}), 404
    return jsonify({"status": 404, "error": "User does not exist!"}), 404

@myquestionerv2.route('/auth/users', methods=['GET'])
def get_all_registered_users():
    ''' method to get all registered users '''
    questioner_users = myuser.get_all_users()
    if questioner_users:
        return jsonify({"status": 200, "Message": "All Users", "data": questioner_users}), 200
    return jsonify({"status": 404, "error": "No users registered yet"}), 404

@myquestionerv2.route('/auth/users/<int:userId>', methods=['GET'])
def get_registered_user(userId):
    ''' method to fetch a single registered user '''
    single_user = myuser.get_a_user(userId)
    if single_user:
        data = request.get_json()
        username = data['username']
        phone = data['phoneNumber']
        email = data['email']
        return jsonify({"status": 200, "Message": "User Found", "data": [{"username": username, "phone": phone, "email": email}]}), 200
    return jsonify({"status": 404, "error": "User not found!"}), 404
    conn.close()
