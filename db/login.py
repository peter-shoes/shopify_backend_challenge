from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user
from db import db,app

# login setup
login_manager = LoginManager()
login_manager.init_app(app)

# create user table
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def attempt_login(username):
    try:
        user = User.query.filter_by(username=username).first()
        login_user(user)
    except:
        return False

