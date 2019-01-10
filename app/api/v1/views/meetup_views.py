from flask import Flask, request, jsonify, Blueprint
from datetime import datetime

mymeets = Blueprint('meet1', __name__, url_prefix='/api/v1')

from ..models.user_models import UserRegistration
from ..models.meetup_models import MeetupRegistration
from ..models.meetup_models import QuestionRegistration
from ..utils.validators import validate_meetup

user = UserRegistration('firstname', 'lastname', 'othername', 'phoneNumber', 'username', 'email', 'password', 'confirm_password', 'isAdmin')
meeting = MeetupRegistration('location', 'images', 'topic', 'happeningOn', 'Tags')
question = QuestionRegistration('questionId', 'userId', 'meetupId', 'title', 'body', 'votes')

@mymeets.route('/meetups', methods=['POST'])
def post_meetup():
    ''' method to post a meetup on the application '''
    data = request.get_json()
    meetupId = len(meeting.All_Meetups) + 1
    location = data['location']
    images = data['images']
    topic = data['topic']
    happeningOn = data['happeningOn']
    Tags = data['Tags']
    createdOn = meeting.createdOn
    meeting.post_a_meetup(meetupId, location, images, topic, happeningOn, Tags, createdOn)
    meetup_validator = validate_meetup(data)

    if (meetup_validator != True):
        return meetup_validator

    return jsonify({"status": 201, "MeetupMessage": "Success", "data": [{"Meetup": topic, "Created On": createdOn, "Meetup Id": meetupId}]}), 201

@mymeets.route('/meetups/<int:meetupId>', methods=['GET'])
def get_meetup(meetupId):
    ''' method to get a single posted meetup '''
    i = meeting.get_a_meetup(meetupId)
    if i:
        return jsonify({"status": 200, "data": [{"Meetup": i}]}), 200
    return jsonify({"status": 404, "error": "Meetup not found!"}), 404

@mymeets.route('/meetups/upcoming', methods=['GET'])
def get_all_posted_meetups():
    ''' method to get all the posted meetups '''
    return jsonify({"All_Meetups": meeting.All_Meetups}), 200

@mymeets.route('/meetups/<int:meetupId>/questions', methods=['POST'])
def post_answer(meetupId):
    ''' method to post questions to a specific meeetup '''
    i = meeting.get_a_meetup(meetupId)
    if i:
        data = request.get_json()
        questionId = len(question.All_Users) + 1
        title = data['title']
        body = data['body']
        anstimeposted = answer.anstimeposted
        answer.post_an_answer(answerId, ansbody, anstimeposted)
        answer_validator = validate_answer(data)

        if (answer_validator != True):
            return answer_validator
        return jsonify({"Message": "question posted successfully", "Status": "Ok"}), 201
    return jsonify({"Message": "Question not found!"}), 404
