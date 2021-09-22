from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopify.db'
app.config['SECRET_KEY'] = 'shopify'
app.config['SQL_TRACK_MODIFICATIONS'] = False
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

db = SQLAlchemy(app)

import database
database.__init__

import routes

# register blueprints
app.register_blueprint(routes.login.login)
app.register_blueprint(routes.upload.upload)

if __name__ == '__main__':
    app.run()
