from datetime import datetime


class UserRegistration():
    ''' class model for the user registration '''
    def __init__(self, firstname, lastname, othername, phoneNumber, username, email, password, confirm_password, isAdmin):
        ''' method to initialize the class model '''
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.phoneNumber = phoneNumber
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.registered = datetime.now()
        self.isAdmin = isAdmin
        self.All_Users = []

    def register_a_user(self, userId, firstname, lastname, othername, phoneNumber, username, email, password, confirm_password, registered, isAdmin):
        ''' method to register a user '''
        my_user = {
            "userId": userId,
            "firstname": firstname,
            "lastname": lastname,
            "othername": othername,
            "phoneNumber": phoneNumber,
            "username": username,
            "email": email,
            "password": password,
            "confirm_password": confirm_password,
            "registered": registered,
            "isAdmin": isAdmin

        }

        self.All_Users.append(my_user)

    def get_a_user(self, userId):
        ''' method to fetch a single user '''
        for usr in self.All_Users:
            if usr['userId'] == userId:
                return usr

    def get_user_email(self, email):
        ''' method to get a user email '''
        for usre in self.All_Users:
            if usre['email'] == email:
                return usre

    def get_username(self, username):
        ''' method to get a username '''
        for usres in self.All_Users:
            if usres['username'] == username:
                return usres

    def find(self, username):
        ''' method to query a username and match it to its assigned password '''
        for usre in self.All_Users:
            if usre['username'] == username:
                return usre['password']

    def login_a_user(self, username, password):
        ''' method to query if a username exists and then matches it to its assigned password '''
        response = self.find(username)
        if response:
            if response == password:
                return True
        return response
