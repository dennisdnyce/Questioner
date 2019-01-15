import os
import unittest
import json

import pytest

from app import create_app
from app.api.v1.models.meetup_models import MeetupRegistration
from app.api.v1.models.question_models import QuestionRegistration
from app.api.v1.views.meetup_views import meeting, question
from app.api.v1.utils.validators import validate_question


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
        del question.All_Questions[:]

    def test_question_empty_title(self):
        ''' tests that a user cannot post a question meetup without title '''
        response = self.client.post("/api/v1/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.post("/api/v1/meetups/1/questions", data=json.dumps(dict(title="", body="this is a body")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("title required", response_msg["error"])

    def test_question_empty_body(self):
        ''' tests that a user cannot post a question meetup without body '''
        response = self.client.post("/api/v1/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.post("/api/v1/meetups/1/questions", data=json.dumps(dict(title="i am andelan", body="")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("body required", response_msg["error"])

    def test_existing_question_upvote(self):
        ''' tests that a user can upvote existing question '''
        response = self.client.post("/api/v1/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.post("/api/v1/meetups/1/questions", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["Question Message"])
        response = self.client.patch("/api/v1/questions/1/upvote", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("upvote success", response_msg["VoteMessage"])

    def test_non_existing_question_upvote(self):
        ''' tests that a user cannot upvote non-existing question '''
        response = self.client.post("/api/v1/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.post("/api/v1/meetups/1/questions", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["Question Message"])
        response = self.client.patch("/api/v1/questions/4/upvote", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Specified question not found!", response_msg["error"])

    def test_existing_question_downvote(self):
        ''' tests that a user can downvote existing question '''
        response = self.client.post("/api/v1/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.post("/api/v1/meetups/1/questions", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["Question Message"])
        response = self.client.patch("/api/v1/questions/1/upvote", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("upvote success", response_msg["VoteMessage"])
        response = self.client.patch("/api/v1/questions/1/downvote", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("downvote success", response_msg["VoteMessage"])

    def test_non_existing_question_downvote(self):
        ''' tests that a user cannot downvote non-existing question '''
        response = self.client.post("/api/v1/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.post("/api/v1/meetups/1/questions", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["Question Message"])
        response = self.client.patch("/api/v1/questions/1/upvote", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response = self.client.patch("/api/v1/questions/4/downvote", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Specified question not found", response_msg["error"])

    def test_existing_question_negative_downvote(self):
        ''' tests that a user cannot downvote existing question to negative value'''
        response = self.client.post("/api/v1/meetups", data=json.dumps(self.meetup), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["MeetupMessage"])
        response = self.client.post("/api/v1/meetups/1/questions", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Success", response_msg["Question Message"])
        response = self.client.patch("/api/v1/questions/1/upvote", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("upvote success", response_msg["VoteMessage"])
        response = self.client.patch("/api/v1/questions/1/downvote", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("downvote success", response_msg["VoteMessage"])
        response = self.client.patch("/api/v1/questions/1/downvote", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("a downvote cannot be negative", response_msg["error"])

''' make tests conveniently executable '''
if __name__ == '__main__':
    unittest.main()
