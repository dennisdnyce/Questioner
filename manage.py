from app.api.v2.models.database import QuestionerDatabaseConnection

connector = QuestionerDatabaseConnection()
connector.create_questioner_tables()
