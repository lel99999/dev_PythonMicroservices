# services/users/project/config.py

import os
import unittest

from flask import current_app
from flask_testing import TestCase

from project import create_app

class BaseConfig:
    """Base cofiguration"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'my_precious'

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
#   SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@users-db:5432/users_dev"


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')
#   SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@users-db:5432/users_test" 

class ProductionConfig(BaseConfig):
    """Production configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
