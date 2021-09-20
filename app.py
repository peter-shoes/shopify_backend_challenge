from flask import Flask, jsonify
from flask_cors import CORS
import db
import routes

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
# config
app.config.from_object(__name__)

# init db
db.__init__

# enable routes
routes.__init__

# register blueprints
app.register_blueprint(routes.login.login)


if __name__ == '__main__':
    app.run()
