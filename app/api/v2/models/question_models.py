from datetime import datetime

from .database import QuestionerDatabaseConnection

class QuestionRegistration(QuestionerDatabaseConnection):
    ''' class for question registration '''
    def __init__(self, title=None, body=None):
        super().__init__()
        db = QuestionerDatabaseConnection
        self.createdOn = datetime.now()
        self.title = title
        self.body = body
        self.votes = 0
        self.cursor = db.cursor_obj(self)

    def post_a_question(self):
        ''' method to post a meetup question '''
        sql = """INSERT INTO questions (title,body)
                 VALUES(%s,%s) RETURNING questionId"""
        self.cursor.execute(sql, (self.title,self.body))

    def get_all_questions(self):
        ''' method to fetch all the posted meetup questions '''
        command = "SELECT * FROM questions"
        self.cursor.execute(command)
        all_questions = self.cursor.fetchall()
        return all_questions

    def get_a_question(self, questionId):
        ''' method to fetch a single meetup question based on its unique id '''
        command = """select * from questions where questionId = %s"""
        self.cursor.execute(command, (questionId, ))
        record = self.cursor.fetchall()
        return record
