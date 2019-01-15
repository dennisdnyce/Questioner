from datetime import datetime

class QuestionRegistration():
    ''' class for question registration '''
    def __init__(self, title, body, votes):
        self.createdOn = datetime.now()
        self.title = title
        self.body = body
        self.votes = 0
        self.All_Questions = []

    def post_a_question(self, questionId, title, body, createdOn, votes):
        ''' method to post a question to a particular meetup '''
        my_question = {
            "questionId": questionId,
            "title": title,
            "body": body,
            "createdOn": createdOn,
            "votes": votes
        }
        self.All_Questions.append(my_question)

    def get_a_question(self, questionId):
        ''' method to fetch a single meetup question based on its unique id '''
        for question_post in self.All_Questions:
            if question_post['questionId'] == questionId:
                return question_post
