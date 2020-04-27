import requests

from flask import g, request
from functools import wraps
from authlib.jose import JsonWebKey, JWK_ALGORITHMS, jwt


def get_subject(f):
    def get_and_load_jwk():
        r = requests.get('http://oathkeeper-api:4456/.well-known/jwks.json')
        key = r.json()['keys'][0]
        jwk = JsonWebKey(algorithms=JWK_ALGORITHMS)
        return jwk.loads(key)

    @wraps(f)
    def subject(*args, **kwargs):
        token = request.headers.get('Authorization').split(' ')[1]
        jwk = get_and_load_jwk()
        sub = jwt.decode(token, jwk)['sub']
        g.current_user_id = sub
        return f(*args, **kwargs)
    return subject
