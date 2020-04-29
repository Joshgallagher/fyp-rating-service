import datetime

from flask import request, abort
from functools import wraps
from authlib.jose import jwt
from .get_jwk import get_jwk

claims_options = {
    'aud': {
        'essential': True,
        'values': ['vue']
    },
    'iss': {
        'essential': True,
        'values': ['http://127.0.0.1:4455/']
    },
    'sub': {
        'essential': True
    }
}


def authorise(f):
    @wraps(f)
    def check(*args, **kwargs):
        try:
            token = request.headers.get('Authorization').split(' ')[1]
            jwk = get_jwk()
            claims = jwt.decode(token, jwk, claims_options=claims_options)
            claims.validate(
                now=datetime.datetime.now().timestamp(), leeway=600)
        except Exception:
            abort(401)
        return f(*args, **kwargs)
    return check
