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

