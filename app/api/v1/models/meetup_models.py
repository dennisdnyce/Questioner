from datetime import datetime

class MeetupRegistration():
    ''' class model for meetup registration '''
    def __init__(self, location, images, topic, happeningOn, Tags):
        self.location = location
        self.images = images
        self.topic = topic
        self.happeningOn = happeningOn
        self.Tags = Tags
        self.createdOn = datetime.now()
        self.All_Meetups = []

    def post_a_meetup(self, meetupId, location, images, topic, createdOn, happeningOn, Tags):
        ''' method to post a meetup '''
        my_meetup = {
            "meetupId": meetupId,
            "createdOn": createdOn,
            "location": location,
            "images": images,
            "topic": topic,
            "happeningOn": happeningOn,
            "Tags": Tags
        }
        self.All_Meetups.append(my_meetup)

    def get_a_meetup(self, meetupId):
        ''' method to get specific meetup based on its id '''
        for meetup in self.All_Meetups:
            if meetup['meetupId'] == meetupId:
                return meetup
