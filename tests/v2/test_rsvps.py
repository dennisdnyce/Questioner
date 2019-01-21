import os
import json
import unittest

import pytest

from app import create_app
from app.api.v2.models.meetup_models import MeetupRegistration
from app.api.v2.models.rsvp_models import RsvpRegistration
from app.api.v2.views.meetup_views import meeting, rsvp
from app.api.v2.utils.validators import validate_meetup, validate_rsvp
from app.api.v2.models.database_test import QuestionerTestDatabase

connector = QuestionerTestDatabase()

class TestMeetRegistration(unittest.TestCase):
    ''' This class represents the User Registration test case '''
    def setUp(self):
        ''' define test variables and initialize the app '''
        self.app = create_app(config='testing')
        self.client = self.app.test_client()
        connector.destroy_questioner_test_tables()
        connector.create_questioner_test_tables()
        self.meetup ={
            'location': 'kitale',
            'images': 'juma.png, wafula.jpg',
            'topic': 'life of pie',
            'happeningOn': '2019/05/12',
            'Tags': 'home, love, passion'
            }

        self.rsvp ={
            'response': 'Yes'
            }

    def test_rsvp_empty_response(self):
        ''' tests that a user cannot make an rsvp with an empty response '''
        response = self.client.post("/api/v2/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.post("/api/v2/meetups/1/rsvps", data=json.dumps(dict(response="")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("its a simple Yes or No question", response_msg["error"])

    def test_rsvp_post_success(self):
        ''' tests that a user cannot make an rsvp with an empty response '''
        response = self.client.post("/api/v2/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.post("/api/v2/meetups/1/rsvps", data=json.dumps(dict(response="yes")), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["RsvpMessage"])

    def test_rsvp_post_success(self):
        ''' tests that a user cannot make an rsvp with an empty response '''
        response = self.client.post("/api/v2/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.post("/api/v2/meetups/12/rsvps", data=json.dumps(dict(response="yes")), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["RsvpMessage"])


    def tearDown(self):
        ''' destroys the test variables after the tests finish executing '''
        connector.destroy_questioner_test_tables()

''' make tests conveniently executable '''
if __name__ == '__main__':
    unittest.main()
