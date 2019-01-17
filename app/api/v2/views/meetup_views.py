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
