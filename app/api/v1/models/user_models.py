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
        self.isAdmin = False
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
        ''' method to fetch a single user based on the user id'''
        for usr in self.All_Users:
            if usr['userId'] == userId:
                return usr

    def get_username(self, username):
        ''' method to get a username on signup to check if it exists'''
        for usres in self.All_Users:
            if usres['username'] == username:
                return usres

    def get_user_email(self, email):
        ''' method to get a user email on signup to check if it exists '''
        for usre in self.All_Users:
            if usre['email'] == email:
                return usre
