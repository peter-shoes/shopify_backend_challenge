from app import app
from flask_sqlalchemy import SQLAlchemy

# instantiate the db
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopify.db'
app.config['SECRET_KEY'] = 'shopify'

from routes import login

db.create_all()