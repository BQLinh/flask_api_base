from flask import Blueprint, jsonify, request

BP = Blueprint('user', __name__)
from schemas.user import user_schema
from models.user import User
from models.base import db

@BP.route('/')
def index():
    data = request.data
    print(data)
    user_schema.load(data)
    return user_schema.dump(User.query.get(1))


@BP.route('/', methods=['POST'])
def create_user():
    data = request.data
    print(data)
    user = User(username='linh', email='linh@gmail.com')
    db.session.add(user)
    db.session.commit()
    return user_schema.dump(user)
