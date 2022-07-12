# services/users/manage.py
import unittest

from flask.cli import FlaskGroup
from project import app, db

cli = FlaskGroup(app)

@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
@cli.command()
def test():
    """Runs the tests without coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
     cli()
