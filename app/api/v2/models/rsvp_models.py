from datetime import datetime

class RsvpRegistration():
    ''' class for RSVP model '''
    def __init__(self, response):
        self.response = response
        self.createdOn = datetime.now()
        self.All_Rsvps = []
