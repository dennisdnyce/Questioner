from datetime import datetime

from .database import QuestionerDatabaseConnection

class RsvpRegistration(QuestionerDatabaseConnection):
    ''' class for RSVP model '''
    def __init__(self, response=None):
        super().__init__()
        db = QuestionerDatabaseConnection
        self.response = response
        self.createdOn = datetime.now()

