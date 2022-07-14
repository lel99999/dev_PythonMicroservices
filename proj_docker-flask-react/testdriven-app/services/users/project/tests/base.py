# services/users/project/tests/base.py

from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from project import create_app, db

app = create_app()

class BaseTestCase(TestCase):
#   db = SQLAlchemy(self._app)
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app
    
    def setUp(self):
        db=SQLAlchemy(create_app(self))
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db=SQLAlchemy(create_app(self))
        db.session.remove()
        db.drop_all()
