import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Course


class UniversityTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = "postgresql://postgres@localhost:5432/flask-api-unit-test-test"
        setup_db(self.app, self.database_path)

        self.new_course = {
            'name': 'Discrete Mathematics',
            'semseter': 2,
        }

        self.new_student = {
            'name': 'Test Student',
            'email': 'student@student.com',
        }

        self.new_professor = {
            'name': 'Test Professor',
            'email': 'professor@professor.com',
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_given_behavior(self):
        """Test _____________ """
        res = self.client().get('/courses')
        self.assertEqual(res.status_code, 200)


# @TODO: Write at least two tests for each endpoint - one each for success and error behavior.
# You can feel free to write additional tests for nuanced functionality,




# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
