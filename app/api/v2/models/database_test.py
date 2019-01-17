import psycopg2
from psycopg2 import extras

class QuestionerTestDatabase(object):
    def __init__(self):
        self.conn = None
        self.cur = None
        self.db = None

    def create_questioner_test_tables(self):
        ''' Creates the questioner test database tables for admin, users, questions, meetups, and rsvps '''
        table_commands = (
            """CREATE TABLE IF NOT EXISTS test_admin(
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
            """INSERT INTO test_admin (firstname,lastname,phoneNumber,username,email,password,isAdmin) \
                  VALUES ('Dennis', 'Juma', '0713714835', 'dennisdnyce', 'jumaspay@gmail.com', 'id28294242', True )
            """,
            """CREATE TABLE IF NOT EXISTS test_users(
                userId  serial PRIMARY KEY,
                registered DATE NOT NULL DEFAULT CURRENT_DATE,
                isAdmin BOOLEAN NOT NULL DEFAULT FALSE,
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                othername TEXT NOT NULL,
                phoneNumber varchar(100) UNIQUE NOT NULL,
                username varchar(100) UNIQUE NOT NULL,
                email varchar(100) UNIQUE NOT NULL,
                password varchar(100) NOT NULL,
                confirm_password varchar(100) NOT NULL
                )
            """,

            """CREATE TABLE IF NOT EXISTS test_meetups(
                meetupId  serial PRIMARY KEY,
                createdOn DATE NOT NULL DEFAULT CURRENT_DATE,
                location TEXT NOT NULL,
                images varchar(250) NOT NULL,
                topic TEXT NOT NULL,
                happeningOn DATE NOT NULL,
                Tags TEXT NOT NULL
                )
            """,
            """CREATE TABLE IF NOT EXISTS test_questions(
                questionId  serial PRIMARY KEY,
                createdOn DATE NOT NULL DEFAULT CURRENT_DATE,
                title varchar(250) NOT NULL,
                body TEXT NOT NULL,
                votes INT NOT NULL DEFAULT 0
                )
            """,
            """CREATE TABLE IF NOT EXISTS test_rsvps(
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
                return 'error connecting to the questioner test database'

    @staticmethod
    def __connection():
        ''' Creates a connection to the database '''
        return psycopg2.connect(
            host="localhost", database="questioner_test", user="tester", password="mytestingpassword", port="5432"
        )

    def get_connection(self):
        ''' Gets the connection parameters specified above '''
        self.db = QuestionerTestDatabase()
        self.conn = self.db.__connection()
        self.conn.autocommit = True
        return self.conn

    def cursor_obj(self):
        ''' Defines the cursor '''
        self.db = QuestionerTestDatabase()
        self.cur = self.db.get_connection().cursor(
            cursor_factory=extras.RealDictCursor)
        return self.cur

    def destroy_questioner_test_tables(self):
        ''' Destroys the database objects '''
        drop_tables = [
            " DROP TABLE IF EXISTS test_admin CASCADE",
            " DROP TABLE IF EXISTS test_users CASCADE",
            " DROP TABLE IF EXISTS test_meetups CASCADE",
            " DROP TABLE IF EXISTS test_questions CASCADE",
            " DROP TABLE IF EXISTS test_rsvps CASCADE"
        ]
        for command in drop_tables:
            cursor = self.cursor_obj()
            if cursor:
                cursor.execute(command)
            else:
                return 'error connecting to the questioner test database'
