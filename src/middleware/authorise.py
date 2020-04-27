import requests

from flask import request, abort
from functools import wraps
from authlib.jose import JsonWebKey, JWK_ALGORITHMS, jwt


def authorise(f):
    def get_and_load_jwk():
        r = requests.get('http://oathkeeper-api:4456/.well-known/jwks.json')
        key = r.json()['keys'][0]
        jwk = JsonWebKey(algorithms=JWK_ALGORITHMS)
        return jwk.loads(key)

    @wraps(f)
    def check(*args, **kwargs):
        token = request.headers.get('Authorization').split(' ')[1]
        jwk = get_and_load_jwk()
        claims = jwt.decode(token, jwk)
        if not claims.validate():
            abort(401)
        return f(*args, **kwargs)
    return check
