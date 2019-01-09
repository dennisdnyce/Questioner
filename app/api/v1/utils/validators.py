from flask import Flask, jsonify
import re

def validate_users(json):
    if not(json["firstname"].strip()):
        return jsonify({"status": 401, "error":"firstname is required"}), 401

    if not(json["lastname"].strip()):
        return jsonify({"status": 401, "error":"lastname is required"}), 401

    if not(json["othername"].strip()):
        return jsonify({"status": 401, "error":"othername is required"}), 401

    if not(json["phoneNumber"].strip()):
        return jsonify({"status": 401, "error":"phoneNumber is required"}), 401

    if not(json["username"].strip()):
        return jsonify({"status": 401, "error":"Username is required"}), 401

    if re.match(r"(^[a-zA-Z0-9_-]{5,12}$)", json["username"].strip()) is None:
        return jsonify({"status": 401, "error":"Invalid username, make sure its 5 to 12 characters long"}), 401

    if not (json["email"].strip()):
        return jsonify({"status": 401, "error":"Email is required"}), 401

    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", json["email"].strip()) is None:
        return jsonify({"status": 401, "error":"Invalid email"}), 401

    if not (json["password"].strip()):
        return jsonify({"status": 401, "error":"Password is required"}), 401

    if (len(json["password"].strip()) < 8 or len(json["password"].strip()) > 12):
        return jsonify({"status": 401, "error":"Password length should be atleast 8 characters long and atmost 12 characters long"}), 401

    if not (json["confirm_password"].strip()):
        return jsonify({"status": 401, "error":"Password confirmation is required"}), 401

    if not (json["password"].strip() == json["confirm_password"].strip()):
        return jsonify({"status": 401, "error":"Password mismatch"}), 401

    if not(json["isAdmin"].strip()):
        return jsonify({"status": 401, "error":"Usertype is required"}), 401    

    return True

def validate_user_login(json):
    if not (json["username"].strip()):
        return jsonify({"status": 401, "error":"username required to log in"}), 401

    if not (json["password"].strip()):
        return jsonify({"status": 401, "error":"password required to log in"}), 401

    return True
