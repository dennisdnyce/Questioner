from datetime import datetime

from flask import Flask, request, jsonify, Blueprint, make_response
from werkzeug.security import generate_password_hash, check_password_hash

from app.api.v1 import myquestioner
from ..models.user_models import UserRegistration
from ..utils.validators import validate_users

user = UserRegistration('firstname', 'lastname', 'othername', 'phoneNumber', 'username', 'email', 'password', 'confirm_password', 'isAdmin')


@myquestioner.route('/auth/signup', methods=['POST'])
def register_user():
    ''' method to register a user on the application '''
    data = request.get_json()
    userId = len(user.All_Users) + 1
    firstname = data['firstname']
    lastname = data['lastname']
    othername = data['othername']
    phoneNumber = data['phoneNumber']

    username = data['username']
    user_username = user.get_username(username)
    if user_username in user.All_Users:
        return make_response(jsonify({"status": 409, "error": "Username already taken!"}), 409)

    email = data['email']
    user_email = user.get_user_email(email)
    if user_email in user.All_Users:
        return make_response(jsonify({"status": 409, "error": "Email address already registered!"}), 409)

    password = data['password']
    confirm_password = data['confirm_password']
    isAdmin = user.isAdmin
    registered = user.registered

    user_validator = validate_users(data)

    if (user_validator != True):
        return user_validator

    user.register_a_user(userId, firstname, lastname, othername, phoneNumber, username, email,
                         generate_password_hash(password), generate_password_hash(confirm_password), registered, isAdmin)

    return jsonify({"status": 201, "RegistrationMessage": "Registration Successful", "data": [{"Welcome": username, "Member Since": registered, "Member Id": userId}]}), 201

@myquestioner.route('/auth/users', methods=['GET'])
def get_all_registered_users():
    ''' method to get all registered users '''
    questioner_users = user.All_Users
    if questioner_users:
        return jsonify({"status": 200, "data": questioner_users}), 200
    return jsonify({"status": 404, "error": "No users registered yet"}), 404

@myquestioner.route('/auth/users/<int:userId>', methods=['GET'])
def get_registered_user(userId):
    ''' method to get a registered user '''
    single_user = user.get_a_user(userId)
    if single_user in user.All_Users:
        data = request.get_json()
        username = data['username']
        email = data['email']
        isAdmin = user.isAdmin
        registered = user.registered
        phoneNumber = data['phoneNumber']
        return jsonify({"status": 200, "Message": "User Found", "data": [{"Member Id": userId, "User": username, "User Email": email, "isAdmin": isAdmin,
                                                                              "registered": registered, "phoneNumber": phoneNumber}]}), 200
    return jsonify({"status": 404, "error": "User not found!"}), 404
