from flask import Flask, request, jsonify, Blueprint
from datetime import datetime

mymeets = Blueprint('meet1', __name__, url_prefix='/api/v1')

from ..models.meetup_models import MeetupRegistration
from ..models.question_models import QuestionRegistration
from ..models.rsvp_models import RsvpRegistration
from ..utils.validators import validate_meetup, validate_question, validate_rsvp

meeting = MeetupRegistration('location', 'images', 'topic', 'happeningOn', 'Tags')
question = QuestionRegistration('title', 'body', 'votes')
rsvp = RsvpRegistration('response')

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

    return jsonify({"status": 201, "MeetupMessage": "Success", "data": [{"topic": topic, "location": location, "Created On": createdOn, "happeningOn": happeningOn, "tags": [Tags], "images": [images]}]}), 201

@mymeets.route('/meetups/<int:meetupId>', methods=['GET'])
def get_meetup(meetupId):
    ''' method to fetch single posted meetup '''
    i = meeting.get_a_meetup(meetupId)
    if i:
        data = request.get_json()
        topic = data['topic']
        location = data['location']
        Tags = data['Tags']
        happeningOn = data['happeningOn']
        return jsonify({"status": 200, "data": [{"title": topic, "location": location, "tags": Tags, "happeningOn": happeningOn, "id": meetupId}]}), 200
    return jsonify({"status": 404, "error": "Meetup not found!"}), 404

@mymeets.route('/meetups/upcoming', methods=['GET'])
def get_all_posted_meetups():
    ''' method to get all the posted meetups '''
    me = meeting.All_Meetups
    if me:
        return jsonify({"status": 200, "data": me}), 200
    return jsonify({"status": 404, "error": "No meetup record found"}), 404

@mymeets.route('/meetups/<int:meetupId>/questions', methods=['POST'])
def post_meetup_question(meetupId):
    ''' method to post a question to a meetup '''
    mt = meeting.get_a_meetup(meetupId)
    if mt:
        data = request.get_json()
        questionId = len(question.All_Questions) + 1
        title = data['title']
        body = data['body']
        createdOn = question.createdOn
        votes = question.votes
        question.post_a_question(questionId, title, body, createdOn, votes)
        quevalidator = validate_question(data)

        if (quevalidator != True):
            return quevalidator

        return jsonify({"status": 201, "Question Message": "Success", "data": [{"votes": votes, "meetup": meetupId, "title": title, "Post Date": createdOn, "body": body}]}), 201
    return jsonify({"status": 404, "error": "Meetup unavailable"}), 404

@mymeets.route('/questions/<int:questionId>/upvote', methods=['PATCH'])
def upvote_a_question(questionId):
    ''' method to upvote a posted question '''
    qn = [qn for qn in question.All_Questions if qn['questionId'] == questionId]
    if qn:
        qn[0]['votes'] = request.json.get('votes', qn[0]['votes'] + 1)
        return jsonify({"status": 201, "data": qn[0], "VoteMessage": "upvote success"}), 201
    return jsonify({"status": 404, "error": "Specified question not found"}), 404

@mymeets.route('/questions/<int:questionId>/downvote', methods=['PATCH'])
def downvote_a_question(questionId):
    ''' method to downvote a posted question '''
    qn = [qn for qn in question.All_Questions if qn['questionId'] == questionId]
    if qn:
        if qn[0]['votes'] > 0:
            qn[0]['votes'] = request.json.get('votes', qn[0]['votes'] - 1)
            return jsonify({"status": 201, "data": qn[0], "VoteMessage": "upvote success"}), 201
        return jsonify({"status": 401, "error": "a downvote cannot be negative"}), 401
    return jsonify({"status": 404, "error": "Specified question not found"}), 404

@mymeets.route('/meetups/<int:meetupId>/rsvps', methods=['POST'])
def make_rsvp(meetupId):
    ''' method to respond to an rsvp '''
    rsv = meeting.get_a_meetup(meetupId)
    if rsv:
        data = request.get_json()
        rsvpId = len(rsvp.All_Rsvps) + 1
        response = data['response']
        createdOn = rsvp.createdOn
        rsvp.make_an_rsvp(rsvpId, response, createdOn)
        rsvp_validator = validate_rsvp(data)

        if (rsvp_validator != True):
            return rsvp_validator

        return jsonify({"status": 201, "RsvpMessage": "Success", "data": [{"meetup": meetupId, "Reservation Date": createdOn, "status": response}]}), 201
    return jsonify({"status": 404, "error": "Meetup unavailable"}), 404
