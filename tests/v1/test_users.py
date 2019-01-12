import pytest
import unittest
import json
import os
from app import create_app


from app.api.v1.models.user_models import UserRegistration
from app.api.v1.views.user_views import user
from app.api.v1.utils.validators import validate_users


class TestUserRegistration(unittest.TestCase):
    ''' This class represents the User Registration test case '''
    def setUp(self):
        ''' define test variables and initialize the app '''
        self.app = create_app(config='testing')
        self.client = self.app.test_client()

        self.user ={
            'firstname': 'dennis',
            'lastname': 'juma',
            'othername': 'wafula',
            'phoneNumber': '0713714835',
            'username': 'dennisdnyce',
            'email': 'jumaspay@gmail.com',
            'password': 'thisispass',
            'confirm_password': 'thisispass',
            'isAdmin': 'True'
            }

    def tearDown(self):
        del user.All_Users[:]


    def test_user_registration(self):
        ''' tests that a user can sign up for an account '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(self.user), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Registration Successful", response_msg["RegistrationMessage"])

    def test_get_all_registered_users(self):
        ''' tests that the records of all registered users can be retrieved '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(self.user), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Registration Successful", response_msg["RegistrationMessage"])
        response2 = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dnyce1",
        phoneNumber='0713714835', isAdmin='True', email="jumaspay3@gmail.com", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response2.status_code, 201)
        response_msg2 = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Registration Successful", response_msg2["RegistrationMessage"])
        response3 = self.client.get("/api/v1/auth/users", content_type="application/json")
        self.assertEqual(response3.status_code, 200)

    def test_get_registered_user(self):
        ''' tests that the records of a registered user can be retrieved '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(self.user), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Registration Successful", response_msg["RegistrationMessage"])
        response2 = self.client.get("/api/v1/auth/users/1", data=json.dumps(dict(userId=1, username="dennisdnyce",
        email="jumaspay@gmail.com", phoneNumber="0713714835", isAdmin="True")), content_type="application/json")
        self.assertEqual(response2.status_code, 200)

    def test_get_non_existing_registered_user(self):
        ''' tests that the records of a registered user can be retrieved '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(self.user), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Registration Successful", response_msg["RegistrationMessage"])
        response2 = self.client.get("/api/v1/auth/users/11", data=json.dumps(dict(userId=1, username="dennisdnyce",
        email="jumaspay@gmail.com")), content_type="application/json")
        self.assertEqual(response2.status_code, 404)

    def test_user_registration_no_firstname(self):
        ''' tests that a user cannot signup without a firstname '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(firstname='', lastname='jumaa', othername='wafula', username="dennisdnyce",
        phoneNumber='0713714835', isAdmin='True', email="jumaspay3@gmail.com", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("firstname is required", response_msg["error"])

    def test_user_registration_no_lastname(self):
        ''' tests that a user cannot signup without a lastname '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(firstname='dennis', lastname='', othername='wafula', username="dennisdnyce",
        phoneNumber='0713714835', isAdmin='True', email="jumaspay3@gmail.com", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("lastname is required", response_msg["error"])

    def test_user_registration_no_othername(self):
        ''' tests that a user cannot signup without othername '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(firstname='dennis', lastname='jumaa', othername='', username="dennisdnyce",
        phoneNumber='0713714835', isAdmin='True', email="jumaspay3@gmail.com", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("othername is required", response_msg["error"])

    def test_user_registration_no_phone(self):
        ''' tests that a user cannot signup without a phone '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(firstname='dennis', lastname='jumaa', othername='wafula', username="dennisdnyce",
        phoneNumber='', isAdmin='True', email="jumaspay3@gmail.com", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("phoneNumber is required", response_msg["error"])

    def test_user_registration_no_username(self):
        ''' tests that a user cannot signup without a username '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="",
        phoneNumber='0713714835', isAdmin='True', email="jumaspay3@gmail.com", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Username is required", response_msg["error"])

    def test_user_registration_invalid_username(self):
        ''' tests that a user cannot signup with an invalid username '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dny",
        phoneNumber='0713714835', isAdmin='True', email="jumaspay3@gmail.com", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 422)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Invalid username, make sure its 5 to 12 characters long", response_msg["error"])

    def test_user_registration_no_password(self):
        ''' tests that a user cannot signup without a password '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dnyce1",
        phoneNumber='0713714835', isAdmin='True', email="jumaspay3@gmail.com", password="", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Password is required", response_msg["error"])

    def test_user_registration_no_password_confirmation(self):
        ''' tests that a user cannot signup without password confirmation '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dnyce1",
        phoneNumber='0713714835', isAdmin='True', email="jumaspay3@gmail.com", password="thisispass", confirm_password="")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Password confirmation is required", response_msg["error"])

    def test_user_registration_password_mismatch(self):
        ''' tests that a user cannot signup without confirming registered password '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dnyce1",
        phoneNumber='0713714835', isAdmin='True', email="jumaspay3@gmail.com", password="thisispass2", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Password mismatch", response_msg["error"])

    def test_user_registration_password_too_short(self):
        ''' tests that a user cannot signup with password length less than 8 characters '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dnyce1",
        phoneNumber='0713714835', isAdmin='True', email="jumaspay3@gmail.com", password="thisisp", confirm_password="thisisp")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Password length should be atleast 8 characters long and atmost 12 characters long", response_msg["error"])

    def test_user_registration_password_too_long(self):
        ''' tests that a user cannot signup with password length more than 12 characters '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dnyce1",
        phoneNumber='0713714835', isAdmin='True', email="jumaspay3@gmail.com", password="thisispasswordlong", confirm_password="thisispasswordlong")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Password length should be atleast 8 characters long and atmost 12 characters long", response_msg["error"])

    def test_user_registration_no_email(self):
        ''' tests that a user cannot signup without an email address '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dnyce1",
        phoneNumber='0713714835', isAdmin='True', email="", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 406)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Email is required", response_msg["error"])

    def test_user_registration_invalid_email1(self):
        ''' tests that a user cannot signup with an invalid email address '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dnyce1",
        phoneNumber='0713714835', isAdmin='True', email="jumaspay", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 422)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Invalid email", response_msg["error"])

    def test_user_registration_invalid_email2(self):
        ''' tests that a user cannot signup with an invalid email address '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dnyce1",
        phoneNumber='0713714835', isAdmin='True', email="jumaspay3@gmail", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 422)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Invalid email", response_msg["error"])

    def test_user_registration_invalid_email3(self):
        ''' tests that a user cannot signup with an invalid email address '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dnyce1",
        phoneNumber='0713714835', isAdmin='True', email="jumaspay3@gmail.", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 422)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Invalid email", response_msg["error"])

    def test_user_registration_username_taken(self):
        ''' tests that a user cannot signup with a username already registered '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(self.user), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Registration Successful", response_msg["RegistrationMessage"])
        response2 = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dennisdnyce",
        phoneNumber='0713714835', isAdmin='True', email="jumaspay3@gmail.com", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response2.status_code, 409)

    def test_user_registration_email_taken(self):
        ''' tests that a user cannot signup with an email already registered '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(self.user), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Registration Successful", response_msg["RegistrationMessage"])
        response2 = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(firstname='dennisa', lastname='jumaa', othername='wafula', username="dnyce1",
        phoneNumber='0713714835', isAdmin='True', email="jumaspay@gmail.com", password="thisispass", confirm_password="thisispass")), content_type="application/json")
        self.assertEqual(response2.status_code, 409)


''' make tests conveniently executable '''
if __name__ == '__main__':
    unittest.main()
