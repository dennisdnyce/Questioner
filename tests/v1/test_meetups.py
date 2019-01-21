import os
import json
import unittest

import pytest

from app import create_app
from app.api.v1.models.meetup_models import MeetupRegistration
from app.api.v1.views.meetup_views import meeting, question
from app.api.v1.utils.validators import validate_meetup


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

        self.question ={
            'title': 'coding is fun',
            'body': 'heard of flask?'
            }

    def tearDown(self):
        del meeting.All_Meetups[:]


    def test_meetup_post(self):
        ''' tests that an admin user cannot post a meetup '''
        response = self.client.post("/api/v1/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])

    def test_meetup_empty_location(self):
        ''' tests that an admin user cannot post a meetup without location '''
        response = self.client.post("/api/v1/meetups", data=json.dumps(dict(Tags="andela", images="me.jpg", topic="life of pie", location="", happeningOn="23-05-1990")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("meetup location required", response_msg["error"])

    def test_meetup_empty_topic(self):
        ''' tests that an admin user cannot post a meetup without topic '''
        response = self.client.post("/api/v1/meetups", data=json.dumps(dict(Tags="andela", images="me.jpg", topic="", location="kitale", happeningOn="23-05-1990")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("topic required", response_msg["error"])

    def test_meetup_empty_happening_date(self):
        ''' tests that an admin user cannot post a meetup without calendar date '''
        response = self.client.post("/api/v1/meetups", data=json.dumps(dict(Tags="andela", images="me.jpg", topic="life of pie", location="kitale", happeningOn="")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("date required", response_msg["error"])

    def test_existing_meetup(self):
        ''' tests that a user can fetch existing meetup '''
        response = self.client.post("/api/v1/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response = self.client.get("/api/v1/meetups/1", data=json.dumps(dict(meetupId=1, topic="andela", location="kitale", Tags="home, love, passion", happeningOn="23-09-2019")), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("success", response_msg["Message"])

    def test_non_existing_meetup(self):
        ''' tests that a user cannot fetch non-existing meetup '''
        response = self.client.post("/api/v1/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response = self.client.get("/api/v1/meetups/2", content_type="application/json")
        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Meetup not found!", response_msg["error"])

    def test_get_all_upcoming_meetups(self):
        ''' tests that a user can fetch all upcoming meetups '''
        response = self.client.post("/api/v1/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.post("/api/v1/meetups", data=json.dumps(dict(meetupId=2, images="youme.jpg", topic="andela2", location="kitale2", Tags="home2, love2, passion2", happeningOn="25-09-2019")), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.get("/api/v1/meetups/upcoming", content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("success!", response_msg["Message"])

    def test_non_existing_upcoming_meetup(self):
        ''' tests that a user cannot fetch non-existing upcoming meetups '''
        response = self.client.get("/api/v1/meetups/upcoming", content_type="application/json")
        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("No meetup record found", response_msg["error"])

    def test_post_question_to_meetup(self):
        ''' tests that a user can post a question to a meetups '''
        response = self.client.post("/api/v1/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.post("/api/v1/meetups/1/questions", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["Question Message"])

    def test_post_question_to_meetup(self):
        ''' tests that a user cannot post a question to a non-existing meetup '''
        response = self.client.post("/api/v1/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.post("/api/v1/meetups/4/questions", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Meetup unavailable", response_msg["error"])

''' make tests conveniently executable '''
if __name__ == '__main__':
    unittest.main()
