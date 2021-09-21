from flask import Blueprint, json, request, jsonify

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])
def login_submit():
    from db.login import User
    content = request.json
    user = User.authenticate(username=content.get('username'), password=content.get('password'))
    if user:
        return jsonify(
            {'status':'success',
            'user':user}
        )
    else:
        return jsonify({'status':'failure'})

@login.route('/create_user', methods=['POST'])
def create_user():
    from db.login import User
    from db.login import create_new_user
    content = request.json
    user = User(content.get('username'), content.get('password'))
    create_new_user(user)


