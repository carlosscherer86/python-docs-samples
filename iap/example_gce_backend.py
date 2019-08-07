# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import platform

import flask

import validate_jwt

import requests

from authentication import has_authorization
from io import BytesIO
from flask import send_file
from flask import Response

URL = 'http://10.128.0.22/'

app = flask.Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if not has_authorization() :
        return 'Unauthorized request.'
    if flask.request.method == 'GET':
        return get_request(path)
    return ''
        

def get_request(path):
    r = requests.get(URL +'/'+ path)
    return resolve_content_type(r)

def resolve_content_type(request):
    try:
        contentType = request.headers['content-type']
        if contentType == 'text/html':
            return request.text 
        if contentType == 'image/png':
            return send_file(BytesIO(request.content), mimetype=contentType)
        if contentType =='text/css':
            return Response(request.text, mimetype=contentType)
        if contentType == 'application/javascript':
            return Response(request.text, mimetype=contentType)
        return request.headers['content-type']
    except:
        return send_file(BytesIO(request.content))

if __name__ == '__main__':
    app.run()
