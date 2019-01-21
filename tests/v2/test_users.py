import os
import json
import unittest

import pytest

from app import create_app
from app.api.v2.models.user_models import UserRegistration
from app.api.v2.views.user_views import myuser
from app.api.v2.utils.validators import validate_users
from app.api.v2.models.database_test import QuestionerTestDatabase

connector = QuestionerTestDatabase()

class TestUserRegistration(unittest.TestCase):
    ''' This class represents the User Registration test case '''
    def setUp(self):
        ''' define test variables and initialize the app '''
        self.app = create_app(config='testing')
        self.client = self.app.test_client()
        connector.destroy_questioner_test_tables()
        connector.create_questioner_test_tables()
        self.user ={
            'firstname': 'dennis',
            'lastname': 'juma',
            'othername': 'wafula',
            'phoneNumber': '0716714835',
            'username': 'dennisd',
            'isAdmin': 'True',
            'email': 'wafula@gmail.com',
            'password': 'thisispass',
            'confirm_password': 'thisispass'
            }


    def test_user_registration_no_firstname(self):
        ''' tests that a user cannot signup without a firstname '''
        response = self.client.post("/api/v2/auth/signup", data=json.dumps(dict(firstname='', lastname='jumaa', othername='wafula', username="dennisdnycd",
        phoneNumber='0713714835', isAdmin='True', email="jumaspayd@gmail.com", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("firstname is required", response_msg["error"])

    def test_user_registration_no_lastname(self):
        ''' tests that a user cannot signup without a lastname '''
        response = self.client.post("/api/v2/auth/signup", data=json.dumps(dict(firstname='dennis', lastname='', othername='wafula', username="dennisdnye",
        phoneNumber='0713714835', isAdmin='True', email="jumaspaye@gmail.com", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("lastname is required", response_msg["error"])

    def test_user_registration_no_othername(self):
        ''' tests that a user cannot signup without othername '''
        response = self.client.post("/api/v2/auth/signup", data=json.dumps(dict(firstname='dennis', lastname='jumaa', othername='', username="dennisdnyf",
        phoneNumber='0713714835', isAdmin='True', email="jumaspayf@gmail.com", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("othername is required", response_msg["error"])

    def test_user_registration_no_phone(self):
        ''' tests that a user cannot signup without a phone '''
        response = self.client.post("/api/v2/auth/signup", data=json.dumps(dict(firstname='dennis', lastname='jumaa', othername='wafula', username="dennisdnyg",
        phoneNumber='', isAdmin='True', email="jumaspayg@gmail.com", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("phoneNumber is required", response_msg["error"])

    def test_user_registration_no_username(self):
        ''' tests that a user cannot signup without a username '''
        response = self.client.post("/api/v2/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="",
        phoneNumber='0713714835', isAdmin='True', email="jumaspayh@gmail.com", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Username is required", response_msg["error"])

    def test_user_registration_invalid_username(self):
        ''' tests that a user cannot signup with an invalid username '''
        response = self.client.post("/api/v2/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dny",
        phoneNumber='0713714835', isAdmin='True', email="jumaspayi@gmail.com", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 422)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Invalid username, make sure its 5 to 12 characters long", response_msg["error"])

    def test_user_registration_no_password(self):
        ''' tests that a user cannot signup without a password '''
        response = self.client.post("/api/v2/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dnyce1j",
        phoneNumber='0713714835', isAdmin='True', email="jumaspayj@gmail.com", password="", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Password is required", response_msg["error"])

    def test_user_registration_no_password_confirmation(self):
        ''' tests that a user cannot signup without password confirmation '''
        response = self.client.post("/api/v2/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dnyce1k",
        phoneNumber='0713714835', isAdmin='True', email="jumaspayk@gmail.com", password="thisispass", confirm_password="")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Password confirmation is required", response_msg["error"])

    def test_user_registration_password_mismatch(self):
        ''' tests that a user cannot signup without confirming registered password '''
        response = self.client.post("/api/v2/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dnyce1l",
        phoneNumber='0713714835', isAdmin='True', email="jumaspayl@gmail.com", password="thisispass2", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Password mismatch", response_msg["error"])

    def test_user_registration_password_too_short(self):
        ''' tests that a user cannot signup with password length less than 8 characters '''
        response = self.client.post("/api/v2/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dnycem2",
        phoneNumber='0713714835', isAdmin='True', email="jumaspaym2@gmail.com", password="thisisp", confirm_password="thisisp")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Password length should be atleast 8 characters long and atmost 12 characters long", response_msg["error"])

    def test_user_registration_password_too_long(self):
        ''' tests that a user cannot signup with password length more than 12 characters '''
        response = self.client.post("/api/v2/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dnyceu1",
        phoneNumber='0713714835', isAdmin='True', email="jumaspayu3n@gmail.com", password="thisispasswordlong", confirm_password="thisispasswordlong")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Password length should be atleast 8 characters long and atmost 12 characters long", response_msg["error"])

    def test_user_registration_no_email(self):
        ''' tests that a user cannot signup without an email address '''
        response = self.client.post("/api/v2/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dnyce1op",
        phoneNumber='0713714835', isAdmin='True', email="", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Email is required", response_msg["error"])

    def test_user_registration_invalid_email1(self):
        ''' tests that a user cannot signup with an invalid email address '''
        response = self.client.post("/api/v2/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dnyceq1",
        phoneNumber='0713714835', isAdmin='True', email="jumaspay", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 422)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Invalid email", response_msg["error"])

    def test_user_registration_invalid_email2(self):
        ''' tests that a user cannot signup with an invalid email address '''
        response = self.client.post("/api/v2/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dnycer1",
        phoneNumber='0713714835', isAdmin='True', email="jumaspay3@gmail", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 422)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Invalid email", response_msg["error"])

    def test_user_registration_invalid_email3(self):
        ''' tests that a user cannot signup with an invalid email address '''
        response = self.client.post("/api/v2/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dnyces1",
        phoneNumber='0713714835', isAdmin='True', email="jumaspay3@gmail.", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 422)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Invalid email", response_msg["error"])

    def tearDown(self):
        ''' destroys the test variables after the tests finish executing '''
        connector.destroy_questioner_test_tables()


''' make tests conveniently executable '''
if __name__ == '__main__':
    unittest.main()
