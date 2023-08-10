"""
BaseTest

This class should be the parent of the non-unit test. It allows for instantiating of the database dynamically.
Make sure that the database is new and blank each time you test to avoid failure.
"""
# Set up runs before every test
# Tear down runs after every test.
from unittest import TestCase
from RestAPI.app import app
from RestAPI.db import db


class BaseTest(TestCase):
    def setUp(self):
        # What it does:
        # Make sure db exists
        # Get a test client
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app) # Initialise app
            db.create_all() # create all tables

        self.app = app.test_client()
        self.app_context = app.app_context()

    def tearDown(self):
        # What this do?
        # Make sure db is blank after test.
        with app.app_context():
            db.session.remove()
            db.drop_all()