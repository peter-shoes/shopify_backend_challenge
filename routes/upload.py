from flask import Blueprint, json, request, jsonify, send_file
from werkzeug.utils import secure_filename, redirect
import os
from shutil import make_archive
upload = Blueprint('upload', __name__)

@upload.route('/upload', methods=['POST'])
def upload_picture():
    username = request.form.get('username')
    uploads_dir = os.path.join('user_photos/', username)
    os.makedirs(uploads_dir, exist_ok=True)
    for fname in request.files:
        f = request.files.get(fname)
        print(f)
        f.save(uploads_dir +'/'+secure_filename(fname))
    return jsonify(
        {'status':'success'}
    )

@upload.route('/get_user_photos/<username>', methods=['GET'])
def get_photos(username):
    try:
        uploads_dir = os.path.join('user_photos/', username)
        return jsonify({'files': [(i) for i in os.listdir(uploads_dir)]})
    except:
        return jsonify({'status':'failure'})

# I'm aware that this is really sloppy
@upload.route('/get_item/<username>/<item>', methods=['GET'])
def get_item(username, item):
    photo = os.path.join('user_photos/', username, item)
    return send_file(photo)

    


