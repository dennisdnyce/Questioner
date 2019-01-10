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
        for meet in self.All_Meetups:
            if meet['meetupId'] == meetupId:
                return meet
