from flask import Flask, jsonify
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

import models
import routes
import schemas
from models import user
from models.base import app


manager = Manager(app)
manager.add_command('db', MigrateCommand)

models.init_app(app)
routes.init_app(app)
schemas.init_app(app)


@app.route('/movies', methods=['GET'])
def list_movies():
    return jsonify({'greet': 'hello'})


if __name__ == '__main__':
    app.run(debug=True)
