from datetime import datetime

from flask import Flask, request, jsonify, Blueprint, make_response
from werkzeug.security import generate_password_hash, check_password_hash

from app.api.v2 import myquestionerv2
from ..models.user_models import UserRegistration
from ..utils.validators import validate_users

myuser = UserRegistration()

@myquestionerv2.route('/auth/signup', methods=['POST'])
def register_user():
    ''' method to register a user on the application '''
    data = request.get_json()
    registered = myuser.registered
    userId = myuser.userId
    isAdmin = myuser.isAdmin
    firstname = data['firstname']
    lastname = data['lastname']
    othername = data['othername']
    phoneNumber = data['phoneNumber']
    username = data['username']
    user_username = myuser.get_username(username)
    if user_username in myuser.get_all_users():
        return make_response(jsonify({"status": 409, "error": "Username already taken!"}), 409)

    email = data['email']
    user_email = myuser.get_user_email(email)
    if user_email in myuser.get_all_users():
        return make_response(jsonify({"status": 409, "error": "Email address already registered!"}), 409)

    password = data['password']
    confirm_password = data['confirm_password']

    user_validator = validate_users(data)

    if (user_validator != True):
        return user_validator

    questioner_user = UserRegistration(firstname, lastname, othername, phoneNumber, username, email, password, confirm_password)

    questioner_user.register_a_user(firstname, lastname, othername, phoneNumber, username, email, generate_password_hash(password), generate_password_hash(confirm_password))

    return jsonify({"status": 201, "RegistrationMessage": "Registration Successful", "data": [{"Welcome": username, "Member Since": registered, "Member Id": userId}]}), 201

@myquestionerv2.route('/auth/users', methods=['GET'])
def get_all_registered_users():
    ''' method to get all registered users '''
    questioner_users = myuser.get_all_users()
    if questioner_users:
        return jsonify({"status": 200, "data": questioner_users}), 200
    return jsonify({"status": 404, "error": "No users registered yet"}), 404

@myquestionerv2.route('/auth/users/<int:userId>', methods=['GET'])
def get_registered_user(userId):
    ''' method to get a registered user '''
    single_user = myuser.get_a_user(userId)
    if single_user in myuser.get_all_users():
        data = request.get_json()
        username = data['username']
        email = data['email']
        isAdmin = data['isAdmin']
        registered = data['registered']
        phoneNumber = data['phoneNumber']
        return jsonify({"status": 200, "Message": "User Found", "data": [{"Member Id": userId, "User": username, "User Email": email, "isAdmin": isAdmin,
                                                                              "registered": registered, "phoneNumber": phoneNumber}]}), 200
    return jsonify({"status": 404, "error": "User not found!"}), 404
