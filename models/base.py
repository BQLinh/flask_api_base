from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

db = SQLAlchemy()
migrate = Migrate(compare_type=True)
migrate_command = MigrateCommand
manager = Manager