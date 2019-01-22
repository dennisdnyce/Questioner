from datetime import datetime

from .database import QuestionerDatabaseConnection


class MeetupRegistration(QuestionerDatabaseConnection):
    ''' class model for meetup registration '''
    def __init__(self, location=None, images=None, topic=None, happeningOn=None, Tags=None):
        super().__init__()
        db = QuestionerDatabaseConnection
        self.location = location
        self.images = images
        self.topic = topic
        self.happeningOn = happeningOn
        self.Tags = Tags
        self.createdOn = datetime.now()
        self.cursor = db.cursor_obj(self)

    def post_a_meetup(self):
        ''' method to post a meetup '''
        sql = """INSERT INTO meetups (location,images,topic,happeningOn,Tags)
                 VALUES(%s,%s,%s,%s,%s) RETURNING meetupId"""
        self.cursor.execute(sql, (self.location,self.images,self.topic,self.happeningOn,self.Tags))

    def get_all_meetups(self):
        ''' method to fetch all the posted meetups '''
        command = "SELECT * FROM meetups"
        self.cursor.execute(command)
        all_meetups = self.cursor.fetchall()
        return all_meetups

    def get_a_meetup(self, meetupId):
        ''' method to get specific meetup based on its id '''
        command = """select * from meetups where meetupId = %s"""
        self.cursor.execute(command, (meetupId, ))
        record = self.cursor.fetchall()
        return record

    def delete_a_meetup(self, meetupId):
        ''' method to delete specific meetup through its id '''
        command = """delete from meetups where meetupId = %s"""
        self.cursor.execute(command, (meetupId, ))
