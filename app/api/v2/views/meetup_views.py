from datetime import datetime

from flask import Flask, request, jsonify, Blueprint

from app.api.v2 import myquestionerv2
from ..models.meetup_models import MeetupRegistration
from ..models.question_models import QuestionRegistration
from ..models.comment_models import CommentRegistration
from ..models.rsvp_models import RsvpRegistration
from ..utils.validators import validate_meetup, validate_question, validate_comment, validate_rsvp

meeting = MeetupRegistration()
question = QuestionRegistration()
comment = CommentRegistration()
rsvp = RsvpRegistration()

@myquestionerv2.route('/meetups', methods=['POST'])
def post_meetup():
    ''' method to post a meetup on the application '''
    data = request.get_json()
    location = data['location']
    images = data['images']
    topic = data['topic']
    happeningOn = data['happeningOn']
    Tags = data['Tags']
    createdOn = meeting.createdOn

    meetup_validator = validate_meetup(data)
    if (meetup_validator != True):
        return meetup_validator
    meetup_post = MeetupRegistration(location, images, topic, happeningOn, Tags)

    meetup_post.post_a_meetup()

    return jsonify({"status": 201, "MeetupMessage": "Success", "data": [{"published":createdOn, "title": topic, "location": location, "images":images, "tags": Tags, "happeningOn": happeningOn}]}), 201

@myquestionerv2.route('/meetups/upcoming', methods=['GET'])
def get_all_posted_meetups():
    ''' method to get all posted meetups'''
    posted_meetups = meeting.get_all_meetups()
    if posted_meetups:
        return jsonify({"status": 200, "Message": "success!", "data": posted_meetups}), 200
    return jsonify({"status": 404, "error message": "No meetups posted yet"}), 404

@myquestionerv2.route('/meetups/<int:meetupId>', methods=['GET'])
def get_meetup(meetupId):
    ''' method to fetch single posted meetup '''
    meetup_post = meeting.get_a_meetup(meetupId)
    if meetup_post:
            return jsonify({"status": 200, "Message": "meetup found", "data": [{"meetup details": meetup_post, "id": meetupId}]}), 200
    return jsonify({"status": 404, "error": "Meetup not found!"}), 404

@myquestionerv2.route('/meetups/<int:meetupId>/rsvps', methods=['POST'])
def make_rsvp(meetupId):
    ''' method to respond to an rsvp '''
    rsvp_post = meeting.get_a_meetup(meetupId)
    if rsvp_post:
        data = request.get_json()
        response = data['response']
        createdOn = rsvp.createdOn

        rsvp_validator = validate_rsvp(data)
        if (rsvp_validator != True):
            return rsvp_validator

        rsvp_post = RsvpRegistration(response)
        rsvp_post.make_an_rsvp()

        return jsonify({"status": 201, "RsvpMessage": "Success", "data": [{"meetup": meetupId, "Reservation Date": createdOn, "status": response}]}), 201
    return jsonify({"status": 404, "error": "Meetup unavailable"}), 404

@myquestionerv2.route('/meetups/<int:meetupId>', methods=['DELETE'])
def delete_meetup(meetupId):
    ''' method to delete a posted meetup '''
    meetup_post = meeting.get_a_meetup(meetupId)
    if meetup_post:
        meeting.delete_a_meetup(meetupId)
        return jsonify({"status": 200, "data": [{"Message": "meetup record deleted successfully"}]}), 200
    return jsonify({"status": 404, "error": "Meetup record does not exist!"}), 404

@myquestionerv2.route('/meetups/<int:meetupId>/questions', methods=['POST'])
def post_meetup_question(meetupId):
    ''' method to post a question to a meetup '''
    meetup_post = meeting.get_a_meetup(meetupId)
    if meetup_post:
        data = request.get_json()
        title = data['title']
        body = data['body']
        createdOn = question.createdOn
        votes = question.votes

        question_validator = validate_question(data)
        if (question_validator != True):
            return question_validator
        question_post = QuestionRegistration(title, body)
        question_post.post_a_question()

        return jsonify({"status": 201, "Question Message": "Success", "data": [{"votes": votes, "meetup": meetupId, "title": title, "Post Date": createdOn, "body": body}]}), 201
    return jsonify({"status": 404, "error": "Meetup unavailable"}), 404

@myquestionerv2.route('/meetups/<int:meetupId>/questions/<int:questionId>', methods=['GET'])
def get_meetup_question(meetupId, questionId):
    ''' method to get a question meetup '''
    meetup_post = meeting.get_a_meetup(meetupId)
    if meetup_post:
        posted_meetups = meeting.get_all_meetups()
        for meetup_post in posted_meetups:
            question_post = question.get_a_question(questionId)
            if question_post:
                return jsonify({"status": 200, "Message": "Question Found", "data": [{"Question details": question_post, "meetup id": meetupId}]}), 200
            return jsonify({"error": "Question not found", "status" : 404}), 404
    return jsonify({"error": "Meetup not found", "status" : 404}), 404

@myquestionerv2.route('/questions/<int:questionId>/upvote', methods=['PATCH'])
def upvote_a_question(questionId):
    ''' method to upvote a posted question '''
    question_downvote = question.get_a_question(questionId)
    if question_downvote:
            question_downvote[0]['votes'] = request.json.get('votes', question_downvote[0]['votes'] + 1)
            return jsonify({"status": 201, "data": question_downvote[0], "VoteMessage": "upvote success"}), 201
    return jsonify({"status": 404, "error": "Specified question not found"}), 404

@myquestionerv2.route('/questions/<int:questionId>/downvote', methods=['PATCH'])
def downvote_a_question(questionId):
    ''' method to downvote a posted question '''
    question_downvote = question.get_a_question(questionId)
    if question_downvote:
            question_downvote[0]['votes'] = request.json.get('votes', question_downvote[0]['votes'] - 1)
            return jsonify({"status": 201, "data": question_downvote[0], "VoteMessage": "downvote success"}), 201
    return jsonify({"status": 404, "error": "Specified question not found"}), 404

@myquestionerv2.route('/meetups/<int:meetupId>/questions/<int:questionId>/comments', methods=['POST'])
def post_question_comment(meetupId, questionId):
    ''' method to post a comment to a question meetup '''
    meetup_post = meeting.get_a_meetup(meetupId)
    if meetup_post:
        posted_meetups = meeting.get_all_meetups()
        for meetup_post in posted_meetups:
            question_post = question.get_a_question(questionId)
            if question_post:
                data = request.get_json()
                body = data['body']
                createdOn = comment.createdOn

                comment_validator = validate_comment(data)
                if (comment_validator != True):
                    return comment_validator
                comment_post = CommentRegistration(body)
                comment_post.post_a_comment()
                return jsonify({"status": 201, "Comment Message": "Success", "data": [{"body": body, "createdOn": createdOn, "meetup id": meetupId, "questionId": questionId}]}), 201
            return jsonify({"status": 404, "error": "question post unavailable"}), 404
    return jsonify({"status": 404, "error": "meetup post unavailable"}), 404
