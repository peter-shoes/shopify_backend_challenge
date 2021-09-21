from flask import Blueprint, json, request, jsonify

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])
def login_submit():
    from database.login import User
    content = request.get_json()
    user = User.authenticate(username=content.get('username'), password=content.get('password'))
    if user:
        return jsonify(
            {'status':'success'}
        )
    else:
        return jsonify({'status':'failure'})

@login.route('/create_user', methods=['POST'])
def create_user():
    from database.login import create_new_user
    content = request.json
    try:
        user = create_new_user(content.get('username'), content.get('password'))
        if user:
            return jsonify(
                {'status':'success'}
            )
        else:
            return jsonify({'status':'failure'})
    except:
        return jsonify({'status':'failure'})
    


