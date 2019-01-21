import os
import json
import unittest

import pytest

from app import create_app
from app.api.v2.models.meetup_models import MeetupRegistration
from app.api.v2.views.meetup_views import meeting, question, comment
from app.api.v2.utils.validators import validate_meetup
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

        self.question ={
            'title': 'coding is fun',
            'body': 'heard of flask?'
            }
     
    def test_meetup_post(self):
        ''' tests that an admin user can post a meetup '''
        response = self.client.post("/api/v2/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])

    def test_meetup_empty_location(self):
        ''' tests that an admin user cannot post a meetup without location '''
        response = self.client.post("/api/v2/meetups", data=json.dumps(dict(location="", images="me.jpg", topic="life of pie", happeningOn="2019/04/12", Tags="live and love")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("meetup location required", response_msg["error"])

    def test_meetup_empty_topic(self):
        ''' tests that an admin user cannot post a meetup without topic '''
        response = self.client.post("/api/v2/meetups", data=json.dumps(dict(location="kitale", images="me.jpg", topic="", happeningOn="2019/04/12", Tags="live and love")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("topic required", response_msg["error"])

    def test_meetup_empty_happening_date(self):
        ''' tests that an admin user cannot post a meetup without calendar date '''
        response = self.client.post("/api/v2/meetups", data=json.dumps(dict(location="kitale", images="me.jpg", topic="life of pie", happeningOn="", Tags="live and love")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("date required", response_msg["error"])

    def test_get_existing_meetup(self):
        ''' tests that a user can fetch existing meetup '''
        response = self.client.post("/api/v2/meetups", data=json.dumps(dict(location="kitale", images="me.jpg", topic="life of pie", happeningOn="2019/12/13", Tags="live and love")), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.get("/api/v2/meetups/2", data=json.dumps(dict(location="kitale", images="me.jpg", topic="life of pie", happeningOn="2019/12/13", Tags="live and love")), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("meetup found", response_msg["Message"])

    def test_non_existing_meetup(self):
        ''' tests that a user cannot fetch non-existing meetup '''
        response = self.client.post("/api/v2/meetups", data=json.dumps(dict(location="kisum city", images="jatelo.jpg", topic="life of pie", happeningOn="2019/12/13", Tags="live and love")), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.get("/api/v1/meetups/23", content_type="application/json")
        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Meetup not found!", response_msg["error"])

    def test_get_all_upcoming_meetups(self):
        ''' tests that a user can fetch all upcoming meetups '''
        response = self.client.post("/api/v2/meetups", data=json.dumps(dict(location="bungoma city", images="jatelo.jpg", topic="life of pie", happeningOn="2019/12/13", Tags="live and love")), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.post("/api/v2/meetups", data=json.dumps(dict(location="kisii city", images="ikongi.jpg", topic="life of pie", happeningOn="2019/12/13", Tags="live and love")), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.get("/api/v2/meetups/upcoming", content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("success!", response_msg["Message"])

    def test_post_question_to_meetup(self):
        ''' tests that a user can post a question to a meetups '''
        response = self.client.post("/api/v2/meetups", data=json.dumps(dict(location="kisii city", images="ikongi.jpg", topic="life of pie", happeningOn="2019/12/13", Tags="live and love")), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.post("/api/v2/meetups/1/questions", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["Question Message"])


    def tearDown(self):
        ''' destroys the test variables after the tests finish executing '''
        connector.destroy_questioner_test_tables()

''' make tests conveniently executable '''
if __name__ == '__main__':
    unittest.main()
