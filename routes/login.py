from flask import Blueprint, request, jsonify

login = Blueprint('login', __name__)

@login.route('/login_submit', methods=['GET','POST'])
def login_submit():
    if request.method == 'GET':
        return('This is a POST method!')
    if request.method == 'POST':
        from db.login import attempt_login
        content = request.json
        if attempt_login(username=content.get('username')):
            return jsonify({'status':'success'})
        else:
            return jsonify({'status':'failure'})

@login.route('/create-user', methods=['POST'])
def create_user():
    