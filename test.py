from functools import wraps
from flask import Flask, request

app = Flask(__name__)

def login_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        # request = kwargs['request']
        print(request.data)
        return f(*args, **kwargs)
    return inner


def permission_required(permission):
    def inner1(f):
        def inner(*args, **kwargs):
            # request = kwargs['request']
            data = request.get_json()
            print(data)
            if data['role'] != permission:
                return 'User dont have permission'

            return f(*args, **kwargs)
        return inner
    return inner1
    



@app.route('/', methods=['POST'])
@permission_required('admin')
@login_required
def index():
    return 'Hello'

if __name__ == '__main__':
    app.run(debug=True)
