from datetime import datetime

from flask import Flask, request, jsonify, Blueprint

from app.api.v2 import myquestionerv2
from ..models.meetup_models import MeetupRegistration
from ..models.question_models import QuestionRegistration
from ..models.rsvp_models import RsvpRegistration
from ..utils.validators import validate_meetup, validate_question, validate_rsvp

meeting = MeetupRegistration('location', 'images', 'topic', 'happeningOn', 'Tags')
question = QuestionRegistration('title', 'body', 'votes')
rsvp = RsvpRegistration('response')

@myquestionerv2.route('/meetups', methods=['POST'])
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

@myquestionerv2.route('/meetups/<int:meetupId>', methods=['GET'])
def get_meetup(meetupId):
    ''' method to fetch single posted meetup '''
    meetup_post = meeting.get_a_meetup(meetupId)
    if meetup_post:
        data = request.get_json()
        topic = data['topic']
        location = data['location']
        Tags = data['Tags']
        happeningOn = data['happeningOn']
        return jsonify({"status": 200, "Message": "success", "data": [{"title": topic, "location": location, "tags": Tags, "happeningOn": happeningOn, "id": meetupId}]}), 200
    return jsonify({"status": 404, "error": "Meetup not found!"}), 404

@myquestionerv2.route('/meetups/upcoming', methods=['GET'])
def get_all_posted_meetups():
    ''' method to get all the posted meetups '''
    meetup = meeting.All_Meetups
    if meetup:
        return jsonify({"status": 200, "Message": "success!", "data": meetup}), 200
    return jsonify({"status": 404, "error": "No meetup record found"}), 404

@myquestionerv2.route('/meetups/<int:meetupId>/questions', methods=['POST'])
def post_meetup_question(meetupId):
    ''' method to post a question to a meetup '''
    meetup_post = meeting.get_a_meetup(meetupId)
    if meetup_post:
        data = request.get_json()
        questionId = len(question.All_Questions) + 1
        title = data['title']
        body = data['body']
        createdOn = question.createdOn
        votes = question.votes
        question.post_a_question(questionId, title, body, createdOn, votes)
        question_validator = validate_question(data)

        if (question_validator != True):
            return question_validator

        return jsonify({"status": 201, "Question Message": "Success", "data": [{"votes": votes, "meetup": meetupId, "title": title, "Post Date": createdOn, "body": body}]}), 201
    return jsonify({"status": 404, "error": "Meetup unavailable"}), 404

@myquestionerv2.route('/meetups/<int:meetupId>/rsvps', methods=['POST'])
def make_rsvp(meetupId):
    ''' method to respond to an rsvp '''
    rsvp_post = meeting.get_a_meetup(meetupId)
    if rsvp_post:
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

@myquestionerv2.route('/questions/<int:questionId>/upvote', methods=['PATCH'])
def upvote_a_question(questionId):
    ''' method to upvote a posted question '''
    question_upvote = [question_upvote for question_upvote in question.All_Questions if question_upvote['questionId'] == questionId]
    if question_upvote:
        question_upvote[0]['votes'] = request.json.get('votes', question_upvote[0]['votes'] + 1)
        return jsonify({"status": 201, "data": question_upvote[0], "VoteMessage": "upvote success"}), 201
    return jsonify({"status": 404, "error": "Specified question not found!"}), 404

@myquestionerv2.route('/questions/<int:questionId>/downvote', methods=['PATCH'])
def downvote_a_question(questionId):
    ''' method to downvote a posted question '''
    question_downvote = [question_downvote for question_downvote in question.All_Questions if question_downvote['questionId'] == questionId]
    if question_downvote:
        if question_downvote[0]['votes'] > 0:
            question_downvote[0]['votes'] = request.json.get('votes', question_downvote[0]['votes'] - 1)
            return jsonify({"status": 201, "data": question_downvote[0], "VoteMessage": "downvote success"}), 201
        return jsonify({"status": 406, "error": "a downvote cannot be negative"}), 406
    return jsonify({"status": 404, "error": "Specified question not found"}), 404
