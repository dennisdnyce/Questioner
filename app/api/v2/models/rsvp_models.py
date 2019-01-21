from datetime import datetime

from .database import QuestionerDatabaseConnection

class RsvpRegistration(QuestionerDatabaseConnection):
    ''' class for RSVP model '''
    def __init__(self, response=None):
        super().__init__()
        db = QuestionerDatabaseConnection
        self.response = response
        self.createdOn = datetime.now()
        self.cursor = db.cursor_obj(self)

    def make_an_rsvp(self):
        ''' method to make a meetup rsvp '''
        sql = """INSERT INTO rsvps (response)
                 VALUES(%s) RETURNING rsvpId"""
        self.cursor.execute(sql, (self.response, ))

    def view_an_rsvp(self, rsvpId):
        ''' method to fetch a single rsvp based on its unique id '''
        command = """select * from rsvps where rsvpId = %s"""
        self.cursor.execute(command, (rsvpId, ))
        record = self.cursor.fetchall()
        return record
