from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
import models
from models.base import app
from models import entity


# app = Flask(__name__)


# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)

models.init_app(app)
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(128), unique=True, nullable=False)
#     email = db.Column(db.String)


# if __name__ == '__main__':
#     manager.run()
