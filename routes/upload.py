from flask import Blueprint, json, request, jsonify
from werkzeug.utils import secure_filename
import os

upload = Blueprint('upload', __name__)

@upload.route('/upload', methods=['POST'])
def upload_picture():
    uploader_username = request.form.get('username')
    uploads_dir = os.path.join('user_photos/', uploader_username)
    os.makedirs(uploads_dir, exist_ok=True)
    for fname in request.files:
        f = request.files.get(fname)
        print(f)
        f.save(uploads_dir +'/'+secure_filename(fname))
    if True:
        return jsonify(
            {'status':'success'}
        )
    else:
        return jsonify({'status':'failure'})

# @login.route('/upload', methods=['POST'])
# def upload():
#     content = request.get_json()
#     print(content)
#     if True:
#         return jsonify(
#             {'status':'success'}
#         )
#     else:
#         return jsonify({'status':'failure'})
    


