import platform
import flask

from authentication import has_authorization
from request_handler import handle_request

app = flask.Flask(__name__)

@app.route('/')
def route_request():
    token = flask.request.args.get('token')
    if not has_authorization(token) :
        return 'Unauthorized request.'
    return handle_request('', flask.request)    

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return handle_request(path, flask.request)

if __name__ == '__main__':
    app.run()
