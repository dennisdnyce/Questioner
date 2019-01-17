from datetime import datetime

import jwt
from werkzeug.security import generate_password_hash, check_password_hash

from .database import QuestionerDatabaseConnection

class UserRegistration(QuestionerDatabaseConnection):
    ''' class model for the user registration '''
    def __init__(self, firstname=None, lastname=None, othername=None, phoneNumber=None, username=None, email=None, password=None, confirm_password=None):
        super().__init__()
        db = QuestionerDatabaseConnection
        self.registered = datetime.now()
        self.isAdmin = False
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.phoneNumber = phoneNumber
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.cursor = db.cursor_obj(self)

    def register_a_user(self,firstname,lastname,othername,phoneNumber,username,email,password,confirm_password):
        ''' method to register a user '''
        sql = """INSERT INTO users (firstname,lastname,othername,phoneNumber,username,email,password,confirm_password)
                 VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
        self.cursor.execute(sql, (self.firstname,self.lastname,self.othername,self.phoneNumber,self.username,self.email,self.password,self.confirm_password))

    def get_all_users(self):
        ''' method to fetch all the registered users '''
        command = "SELECT * FROM users"
        self.cursor.execute(command)
        all_users = self.cursor.fetchall()
        return all_users

    def get_username(self, username):
        ''' method to get a username on signup to check if it exists'''
        command = "SELECT * FROM users WHERE username = '%s'" % (username)
        self.cursor.execute(command)
        user_name = self.cursor.fetchall()
        return user_name

    def get_user_email(self, email):
        ''' method to get a user email on signup to check if it exists '''
        command = "SELECT * FROM users WHERE email = '%s'" % (email)
        self.cursor.execute(command)
        user_email = self.cursor.fetchall()
        return user_email

    def get_user_phone(self, phoneNumber):
        ''' method to get a user phone number on signup to check if it exists '''
        command = "SELECT * FROM users WHERE phoneNumber = '%s'" % (phoneNumber)
        self.cursor.execute(command)
        user_phone = self.cursor.fetchall()
        return user_phone
