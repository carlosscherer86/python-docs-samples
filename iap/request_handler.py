import requests
from flask import send_file
from flask import Response
from io import BytesIO

GET_METHOD = 'GET'
URL = 'https://34.66.62.85:8080'

def handle_request(path, request):
    if request.method == GET_METHOD:
        return get_request(path, request)
    return ''

def get_request(path, request):
    params = get_parms(request)
    r = requests.get(URL + path + params, verify=False)
    return resolve_content_type(r)

def get_parms(request):
    params = '';
    if len(request.args) > 0:
        params = '?'
        for f in request.args:
            params = params + f + '=' + request.args.get(f) + '&'
    print(params)
    return params

def resolve_content_type(request):
    try:
        contentType = request.headers['content-type']
        if contentType == 'image/png' or contentType == 'image/gif':
            return send_file(BytesIO(request.content), mimetype=contentType)
        return Response(request.text, mimetype=contentType)
    except:
        return request.content