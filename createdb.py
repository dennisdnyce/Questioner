from app.api.v2.models.database import QuestionerDatabaseConnection
from app.api.v2.models.database_test import QuestionerTestDatabase

connector = QuestionerDatabaseConnection()
TestConnector = QuestionerTestDatabase()

connector.create_questioner_tables()
TestConnector.create_questioner_test_tables()
