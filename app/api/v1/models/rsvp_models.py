class RsvpRegistration():
    ''' class for RSVP model '''
    def __init__(self, meetupId, userId, response):
        self.meetupId = meetupId
        self.userId = userId
        self.response = response
        self.All_Rsvps = []

    def make_an_rsvp(self, rsvpId, meetupId, userId, response):
        my_rsvp = {
            "rsvpId": rsvpId,
            "meetupId": meetupId,
            "userId": userId,
            "response": response
        }
        self.All_Rsvps.append(my_rsvp)
