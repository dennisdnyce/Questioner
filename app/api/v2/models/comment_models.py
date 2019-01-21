from datetime import datetime

from .database import QuestionerDatabaseConnection

class CommentRegistration(QuestionerDatabaseConnection):
    ''' class for question registration '''
    def __init__(self, body=None):
        super().__init__()
        db = QuestionerDatabaseConnection
        self.createdOn = datetime.now()
        self.body = body
        self.cursor = db.cursor_obj(self)

    def post_a_comment(self):
        ''' method to post a meetup question comment '''
        sql = """INSERT INTO comments (body)
                 VALUES(%s) RETURNING commentId"""
        self.cursor.execute(sql, (self.body, ))

    def get_a_comment(self, commentId):
        ''' method to fetch a single meetup question comment based on its unique id '''
        command = """select * from comments where commentId = %s"""
        self.cursor.execute(command, (commentId, ))
        record = self.cursor.fetchall()
        return record
