import platform
import flask

from authentication import has_authorization
from request_handler import RequestHandler


app = flask.Flask(__name__)

@app.route('/')
@app.route('/search')
@app.route('/xml')
def need_authorization_routes():
    token = flask.request.args.get('token')
    if not has_authorization(token) :
        return 'Unauthorized request.'
    requestHandler = RequestHandler(token)
    return requestHandler.handle_request(flask.request.path, flask.request, True)    

@app.route('/<path:path>')
def catch_all(path):
    requestHandler = RequestHandler('')
    return requestHandler.handle_request(flask.request.path, flask.request, False)

if __name__ == '__main__':
    app.run()
