import psycopg2
from psycopg2 import extras

class QuestionerDatabaseConnection(object):
    '''class responsible for the connection to the questioner database'''
    def __init__(self):
        self.conn = None
        self.cur = None
        self.db = None

    def create_questioner_tables(self):
        ''' Creates the questioner database tables for admin, users, questions, meetups, and rsvps '''
        table_commands = (
            """CREATE TABLE IF NOT EXISTS admin(
                adminId serial PRIMARY KEY,
                createdOn DATE NOT NULL DEFAULT CURRENT_DATE,
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                phoneNumber varchar(100) NOT NULL,
                username varchar(100) NOT NULL,
                email varchar(100) NOT NULL,
                password varchar(100) NOT NULL,
                isAdmin BOOLEAN NOT NULL DEFAULT TRUE
                )
            """,
            """INSERT INTO admin (firstname,lastname,phoneNumber,username,email,password,isAdmin) \
                  VALUES ('Dennis', 'Juma', '0713714835', 'dennisdnyce', 'jumaspay@gmail.com', 'id28294242', True )
            """,
            """CREATE TABLE IF NOT EXISTS users(
                userId  serial PRIMARY KEY,
                registered DATE NOT NULL DEFAULT CURRENT_DATE,
                isAdmin BOOLEAN NOT NULL DEFAULT FALSE,
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                othername TEXT NOT NULL,
                phoneNumber varchar(100) NOT NULL,
                username varchar(100) NOT NULL,
                email varchar(100) NOT NULL,
                password varchar(100) NOT NULL,
                confirm_password varchar(100) NOT NULL
                )
            """,

            """CREATE TABLE IF NOT EXISTS meetups(
                meetupId  serial PRIMARY KEY,
                createdOn DATE NOT NULL DEFAULT CURRENT_DATE,
                location TEXT NOT NULL,
                images varchar(250),
                topic TEXT NOT NULL,
                happeningOn DATE NOT NULL,
                Tags varchar(250)
                )
            """,
            """CREATE TABLE IF NOT EXISTS questions(
                questionId  serial PRIMARY KEY,
                createdOn DATE NOT NULL DEFAULT CURRENT_DATE,
                title varchar(250) NOT NULL,
                body TEXT NOT NULL,
                votes INT NOT NULL DEFAULT 0
                )
            """,
            """CREATE TABLE IF NOT EXISTS comments(
                commentId  serial PRIMARY KEY,
                createdOn DATE NOT NULL DEFAULT CURRENT_DATE,
                body TEXT NOT NULL
                )
            """,
            """CREATE TABLE IF NOT EXISTS rsvps(
                rsvpId  serial PRIMARY KEY,
                createdOn DATE NOT NULL DEFAULT CURRENT_DATE,
                response varchar(15) NOT NULL
                )
            """
        )
        for command in table_commands:
            cursor = self.cursor_obj()
            if cursor:
                cursor.execute(command)
            else:
                return 'error connecting to the questioner database'

    @staticmethod
    def __connection():
        ''' Creates a connection to the database '''
        return psycopg2.connect(
            host="localhost", database="questioner", user="questioneruser", password="id28294242", port="5432"
        )

    def get_connection(self):
        ''' Gets the database connection parameters specified above '''
        self.db = QuestionerDatabaseConnection()
        self.conn = self.db.__connection()
        self.conn.autocommit = True
        return self.conn

    def cursor_obj(self):
        ''' Defines the cursor that instanciates a connection to the database '''
        self.db = QuestionerDatabaseConnection()
        self.cur = self.db.get_connection().cursor(
            cursor_factory=extras.RealDictCursor)
        return self.cur

    def destroy_questioner_tables(self):
        ''' Destroys the database objects '''
        drop_tables = [
            " DROP TABLE IF EXISTS admin CASCADE",
            " DROP TABLE IF EXISTS users CASCADE",
            " DROP TABLE IF EXISTS meetups CASCADE",
            " DROP TABLE IF EXISTS questions CASCADE",
            " DROP TABLE IF EXISTS comments CASCADE",
            " DROP TABLE IF EXISTS rsvps CASCADE"
        ]
        for command in drop_tables:
            cursor = self.cursor_obj()
            if cursor:
                cursor.execute(command)
            else:
                return 'error connecting to the questioner database'
