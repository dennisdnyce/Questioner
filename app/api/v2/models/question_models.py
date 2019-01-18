from datetime import datetime

class QuestionRegistration():
    ''' class for question registration '''
    def __init__(self, title, body, votes):
        self.createdOn = datetime.now()
        self.title = title
        self.body = body
        self.votes = 0
        self.All_Questions = []
