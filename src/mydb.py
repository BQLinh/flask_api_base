# from sqlalchemy import create_engine

# from sqlalchemy import Column, String, Integer
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker


# engine = create_engine('mysql+mysqldb://linh:1234@mysql-app/my_db')
# base = declarative_base()


# class Users(base):
#     __tablename__ = 'users'

#     user_id = Column(Integer, primary_key=True)
#     date = Column(Integer)
#     item_id = Column(Integer)


# base.metadata.create_all(engine)


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ..app import app
db = SQLAlchemy

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)


with app.app_context():
    db.create_all()