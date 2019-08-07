import platform
import flask
import validate_jwt
import requests

from authentication import has_authorization
from io import BytesIO
from flask import send_file
from flask import Response

URL = 'http://10.181.192.40:8430/avs/'
GET_METHOD = 'GET'

app = flask.Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    token = flask.request.args.get('token')
    if not has_authorization(token) :
        return 'Unauthorized request.'
    if flask.request.method == GET_METHOD:
        return get_request(path)
    return ''
        
def get_request(path):
    r = requests.get(URL +'/'+ path)
    return resolve_content_type(r)

def resolve_content_type(request):
    try:
        contentType = request.headers['content-type']
        if contentType == 'image/png':
            return send_file(BytesIO(request.content), mimetype=contentType)
        return Response(request.text, mimetype=contentType)
    except:
        return request.content

if __name__ == '__main__':
    app.run()
