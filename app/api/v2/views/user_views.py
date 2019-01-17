from datetime import datetime

from flask import Flask, request, jsonify, Blueprint, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import psycopg2
from app.api.v2 import myquestionerv2
from ..models.user_models import UserRegistration
from ..utils.validators import validate_users

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

    questioner_user.register_a_user(firstname, lastname, othername, phoneNumber, username, email, generate_password_hash(password), generate_password_hash(confirm_password))


    return jsonify({"status": 201, "RegistrationMessage": "Registration Successful", "data": [{"Welcome": username, "token": access_token, "Member Since": registered}]}), 201

@myquestionerv2.route('/auth/users', methods=['GET'])
def get_all_registered_users():
    ''' method to get all registered users '''
    questioner_users = myuser.get_all_users()
    if questioner_users:
        return jsonify({"status": 200, "data": questioner_users}), 200
    return jsonify({"status": 404, "error": "No users registered yet"}), 404

@myquestionerv2.route('/auth/users/<int:userId>', methods=['GET'])
def get_registered_user(userId):
    ''' method to fetch a single registered user '''
    conn = psycopg2.connect(host="localhost", database="questioner", user="questioneruser", password="id28294242", port="5432")
    cur = conn.cursor()
    user_query = """select * from users where userid = %s"""
    cur.execute(user_query, (userId, ))
    record = cur.fetchall()
    for row in record:
        user_Id = row[0]
        registered = row[1]
        username = row[7]

        return jsonify({"status": 200, "Message": "User Found", "data": [{"Member Id": user_Id, "Registered On": registered, "username": username}]}), 200
    return jsonify({"status": 404, "error": "User not found!"}), 404
    conn.close()
