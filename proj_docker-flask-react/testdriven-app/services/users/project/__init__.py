# /services/users/project/__init__.py

import sys
import os
import datetime
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON

# instantiate app
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.config.from_object('project.config.DevelopmentConfig')

# set config
app_settings=os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(app)

def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)
    
    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    
    # set up extensions
    db.init_app(app)
    
    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)
    
    # shell context for flask cli
    app.shell_context_processor({'app':app, 'db':db})
    return app

# model
##  class User(db.Model):
##      __tablename__ = "users"
##      id = db.Column(db.Integer, primary_key=True, autoincrement=True)
##      username = db.Column(db.String(128), nullable=False)
##      email = db.Column(db.String(128), nullable=False)
##      active = db.Column(db.Boolean(), default=True, nullable=False)
##  
##  print(app.config, file=sys.stderr)
##  
##  @app.route('/users/ping', methods=['GET'])
##  def ping_pong():
##      return jsonify({
##          'status': 'success',
##          'message': 'pong'
##      })
