from datetime import datetime

class RsvpRegistration():
    ''' class for RSVP model '''
    def __init__(self, response):
        self.response = response
        self.createdOn = datetime.now()
        self.All_Rsvps = []

    def make_an_rsvp(self, rsvpId, response, createdOn):
        my_rsvp = {
            "rsvpId": rsvpId,
            "response": response,
            "createdOn": createdOn
        }
        self.All_Rsvps.append(my_rsvp)

    def view_an_rsvp(self, rsvpId):
        for rev in self.All_Rsvps:
            if rev['rsvpId'] == rsvpId:
                return rev
