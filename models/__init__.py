from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models.base import db, migrate, migrate_command, manager

def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)
    mngr = manager(app)
    mngr.add_command('db', migrate_command)