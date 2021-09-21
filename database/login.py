from flask import Flask
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, app

# login setup
login_manager = LoginManager()
login_manager.init_app(app)

# create user table
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    # initialize username and password for object(row)
    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password, 'sha256')
        
    
    # method for authentication
    @classmethod
    def authenticate(cls, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')

        if not username or not password:
            return None
        
        user = cls.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return None
        
        return user

    def to_dict(self):
        return dict(
            id=self.id,
            username=self.username
        )


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_new_user(username, password):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict())


db.create_all()