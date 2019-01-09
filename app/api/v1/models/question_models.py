from datetime import datetime

class QuestionRegistration():
    ''' class for question registration '''
    def __init__(self, createdBy, meetup, title, body, votes):
        self.createdOn = datetime.now()
        self.createdBy = userId
        self.meetup = meetupId
        self.title = title
        self.body = body
        self.votes = votes
        self.All_Questions = []

    def post_a_question(self, questionId, userId, meetupId, title, body, votes):
        my_question = {
            "questionId": questionId,
            "userId": userId,
            "meetupId": meetupId,
            "title": title,
            "body": body,
            "votes": votes
        }
        self.All_Questions.append(my_question)
