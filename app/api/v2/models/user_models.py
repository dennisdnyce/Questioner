from datetime import datetime

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

    def register_a_user(self):
        ''' method to register a user '''
        sql = """INSERT INTO users (firstname,lastname,othername,phoneNumber,username,email,password,confirm_password)
                 VALUES(%s,%s,%s,%s,%s,%s,%s,%s) RETURNING userId"""
        self.cursor.execute(sql, (self.firstname,self.lastname,self.othername,self.phoneNumber,self.username,self.email,self.password,self.confirm_password))

    def get_all_users(self):
        ''' method to fetch all the registered users '''
        command = "SELECT firstname, lastname, othername, phoneNumber, username, email FROM users"
        self.cursor.execute(command)
        all_users = self.cursor.fetchall()
        return all_users

    def get_a_user(self, userId):
        ''' method to get a username on signup to check if he/she exists'''
        command = """select * from users where userid = %s"""
        self.cursor.execute(command, (userId, ))
        record = self.cursor.fetchall()
        return record
