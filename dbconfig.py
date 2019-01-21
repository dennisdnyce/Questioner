from app.api.v2.models.database import QuestionerDatabaseConnection
from app.api.v2.models.database_test import QuestionerTestDatabase

destroyer = QuestionerDatabaseConnection()
Testdestroyer = QuestionerTestDatabase()

destroyer.destroy_questioner_tables()
Testdestroyer.destroy_questioner_test_tables()
