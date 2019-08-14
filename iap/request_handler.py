import requests
from flask import send_file
from flask import Response
from io import BytesIO
from response_html_handler import add_token

class RequestHandler:
    GET_METHOD = 'GET'
    URL = 'https://34.66.62.85:8080'
    token = '';
    shouldInsertToken = False

    def __init__(self, token): 
        self.token = token

    def handle_request(self, path, request, shouldInsertToken):
        self.shouldInsertToken = shouldInsertToken
        if request.method == self.GET_METHOD:
            return self.get_request(path, request)
        return ''

    def get_request(self,path, request):
        params = self.get_parms(request)
        r = requests.get(self.URL + path + params, verify=False)
        return self.resolve_content_type(r)

    def get_parms(self, request):
        params = '';
        if len(request.args) > 0:
            params = '?'
            for f in request.args:
                params = params + f + '=' + request.args.get(f) + '&'
        return params

    def resolve_content_type(self, request):
        try:
            contentType = request.headers['content-type']
            if contentType == 'image/png' or contentType == 'image/gif':
                return send_file(BytesIO(request.content), mimetype=contentType)
            responseText = request.text
            if self.shouldInsertToken:
                responseText = add_token(request.text, self.token)
            return Response(responseText, mimetype=contentType)
        except:
            return request.content