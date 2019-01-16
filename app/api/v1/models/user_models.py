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
        ''' method to fetch a single user based on the user id '''
        for single_user in self.All_Users:
            if single_user['userId'] == userId:
                return single_user

    def get_username(self, username):
        ''' method to get a username on signup to check if it exists '''
        for user_username in self.All_Users:
            if user_username['username'] == username:
                return user_username

    def get_user_email(self, email):
        ''' method to get a user email on signup to check if it exists '''
        for user_email in self.All_Users:
            if user_email['email'] == email:
                return user_email

    def get_user_phone(self, phoneNumber):
        ''' method to get a user phone number on signup to check if it exists '''
        for user_phone in self.All_Users:
            if user_phone['phoneNumber'] == phoneNumber:
                return user_phone
