from google.oauth2 import id_token
from google.auth.transport import requests
from datetime import datetime

CLIENT_ID_1 = '242715444435-ss081r800k4ib43o4cusd3au76bktfb3.apps.googleusercontent.com'
CLIENT_ID_2 = '593881631501-9ah6is5851aass4lonh1lptc69slfo0e.apps.googleusercontent.com'

def has_authorization(token):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request())
        if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2]:
            raise ValueError('Could not verify audience.')

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

        return isUserValid(idinfo)
    except ValueError as e:
        print(e)
        return False
        pass

def isUserValid(idinfo):
    valid = idinfo['hd'] == 'motorola.com'
    return valid