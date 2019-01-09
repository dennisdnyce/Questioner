import pytest
import unittest
from app import create_app
from flask import Flask
import instance


class TestConfig(unittest.TestCase):
    ''' tests the default configuration environment '''
    def test_config(self):
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(instance.config.Config)
        self.assertTrue(app.config['DEBUG'] is False)
        self.assertTrue(app.config['CSRF_ENABLED'] is True)
        self.assertTrue(app.config['SECRET_KEY'] is 'thisismysecretkeywhydontyouuseyours')

    def test_development(self):
        ''' tests the configuration for the development environment '''
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(instance.config.DevelopmentConfig)
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(app.config['TESTING'] is True)

    def test_staging(self):
        ''' tests the configuration for the staging environment '''
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(instance.config.StagingConfig)
        self.assertTrue(app.config['DEBUG'] is True)

    def test_testing(self):
        ''' tests the configuration for the testing environment '''
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(instance.config.TestingConfig)
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(app.config['TESTING'] is True)

    def test_production(self):
        ''' tests the configuration for the production environment '''
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(instance.config.ProductionConfig)
        self.assertTrue(app.config['DEBUG'] is False)
        self.assertTrue(app.config['TESTING'] is False)

if __name__ == '__main__':
    unittest.main()
