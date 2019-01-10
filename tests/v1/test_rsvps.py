import pytest
import unittest
import json
import os
from app import create_app


from app.api.v1.models.meetup_models import MeetupRegistration
from app.api.v1.models.rsvp_models import RsvpRegistration
from app.api.v1.views.meetup_views import meeting, rsvp
from app.api.v1.utils.validators import validate_rsvp


class TestUserRegistration(unittest.TestCase):
    ''' This class represents the User Registration test case '''
    def setUp(self):
        ''' define test variables and initialize the app '''
        self.app = create_app(config='testing')
        self.client = self.app.test_client()

        self.meetup ={
            'location': 'kitale',
            'images': 'juma.png, wafula.jpg',
            'topic': 'life of pie',
            'happeningOn': '23-09-2018',
            'Tags': 'home, love, passion'
            }

        self.rsvp ={
            'response': 'Yes'
            }

    def tearDown(self):
        del meeting.All_Meetups[:]
        del rsvp.All_Rsvps[:]

    def test_rsvp_empty_response(self):
        ''' tests that a user cannot make an rsvp with an empty response '''
        response = self.client.post("/api/v1/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response = self.client.post("/api/v1/meetups/1/rsvps", data=json.dumps(dict(response="")), content_type="application/json")
        self.assertEqual(response.status_code, 401)

    def test_post_rsvp(self):
        ''' tests that a user can make an rsvp  '''
        response = self.client.post("/api/v1/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response = self.client.post("/api/v1/meetups/1/rsvps", data=json.dumps(dict(response="yes")), content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_post_rsvp_no_meetup(self):
        ''' tests that a user cannot make an rsvp to a non-existing meetup  '''
        response = self.client.post("/api/v1/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response = self.client.post("/api/v1/meetups/66/rsvps", data=json.dumps(dict(response="yes")), content_type="application/json")
        self.assertEqual(response.status_code, 404)
