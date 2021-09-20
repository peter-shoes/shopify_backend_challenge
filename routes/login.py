from flask import Blueprint, request

login = Blueprint('login', __name__)

@login.route('/login_submit', methods=['GET','POST'])
def login_submit():
    if request.method == 'GET':
        return('This is a POST method!')
    if request.method == 'POST':
        from db.login import attempt_login
        data = request.get_json()
        print(data)
        return data
        # return attempt_login(username=data.username)