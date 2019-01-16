import re
import datetime

from flask import Flask, jsonify

def validate_users(json):
    if not(json["firstname"].strip()):
        return jsonify({"status": 406, "error":"firstname is required"}), 406

    if not(json["lastname"].strip()):
        return jsonify({"status": 406, "error":"lastname is required"}), 406

    if not(json["othername"].strip()):
        return jsonify({"status": 406, "error":"othername is required"}), 406

    if not(json["phoneNumber"].strip()):
        return jsonify({"status": 406, "error":"phoneNumber is required"}), 406

    if not(json["username"].strip()):
        return jsonify({"status": 406, "error":"Username is required"}), 406

    if re.match(r"(^[a-zA-Z0-9_-]{5,12}$)", json["username"].strip()) is None:
        return jsonify({"status": 422, "error":"Invalid username, make sure its 5 to 12 characters long"}), 422

    if not (json["email"].strip()):
        return jsonify({"status": 406, "error":"Email is required"}), 406

    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", json["email"].strip()) is None:
        return jsonify({"status": 422, "error":"Invalid email"}), 422

    if not (json["password"].strip()):
        return jsonify({"status": 406, "error":"Password is required"}), 406

    if (len(json["password"].strip()) < 8 or len(json["password"].strip()) > 12):
        return jsonify({"status": 406, "error":"Password length should be atleast 8 characters long and atmost 12 characters long"}), 406

    if not (json["confirm_password"].strip()):
        return jsonify({"status": 406, "error":"Password confirmation is required"}), 406

    if not (json["password"].strip() == json["confirm_password"].strip()):
        return jsonify({"status": 406, "error":"Password mismatch"}), 406

    return True


def validate_user_login(json):
    if not (json["username"].strip()):
        return jsonify({"status": 406, "error":"username required to log in"}), 406

    if not (json["password"].strip()):
        return jsonify({"status": 406, "error":"password required to log in"}), 406

    return True

def validate_meetup(json):
    if not (json["location"].strip()):
        return jsonify({"status": 406, "error":"meetup location required"}), 406

    if not (json["topic"].strip()):
        return jsonify({"status": 406, "error":"topic required"}), 406

    if not (json["happeningOn"].strip()):
        return jsonify({"status": 406, "error":"date required"}), 406

    return True

def validate_question(json):
    if not (json["title"].strip()):
        return jsonify({"status": 406, "error":"title required"}), 406

    if not (json["body"].strip()):
        return jsonify({"status": 406, "error":"body required"}), 406

    return True

def validate_rsvp(json):
    if not (json["response"].strip()):
        return jsonify({"status": 406, "error":"its a simple Yes or No question"}), 406

    return True
