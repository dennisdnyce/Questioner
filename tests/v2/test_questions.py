import os
import json
import unittest

import pytest

from app import create_app
from app.api.v2.models.meetup_models import MeetupRegistration
from app.api.v2.models.question_models import QuestionRegistration
from app.api.v2.views.meetup_views import meeting, question, comment
from app.api.v2.utils.validators import validate_meetup, validate_question
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

    def test_question_empty_title(self):
        ''' tests that a user cannot post a question meetup without title '''
        response = self.client.post("/api/v2/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.post("/api/v2/meetups/1/questions", data=json.dumps(dict(title="", body="this is a body")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("title required", response_msg["error"])

    def test_question_empty_body(self):
        ''' tests that a user cannot post a question meetup without body '''
        response = self.client.post("/api/v2/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.post("/api/v2/meetups/1/questions", data=json.dumps(dict(title="i am andelan", body="")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("body required", response_msg["error"])

    def test_existing_question_upvote(self):
        ''' tests that a user can upvote existing question '''
        response = self.client.post("/api/v2/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.post("/api/v2/meetups/1/questions", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["Question Message"])
        response = self.client.patch("/api/v2/questions/1/upvote", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("upvote success", response_msg["VoteMessage"])

    def test_existing_question_downvote(self):
        ''' tests that a user can downvote existing question '''
        response = self.client.post("/api/v2/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.post("/api/v2/meetups/1/questions", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["Question Message"])
        response = self.client.patch("/api/v2/questions/1/upvote", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("upvote success", response_msg["VoteMessage"])
        response = self.client.patch("/api/v2/questions/1/downvote", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("downvote success", response_msg["VoteMessage"])


    def tearDown(self):
        ''' destroys the test variables after the tests finish executing '''
        connector.destroy_questioner_test_tables()

''' make tests conveniently executable '''
if __name__ == '__main__':
    unittest.main()
