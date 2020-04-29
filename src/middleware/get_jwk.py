import requests

from authlib.jose import JsonWebKey, JWK_ALGORITHMS


def get_jwk():
    r = requests.get('http://oathkeeper-api:4456/.well-known/jwks.json')
    key = r.json()['keys'][0]
    jwk = JsonWebKey(algorithms=JWK_ALGORITHMS)
    return jwk.loads(key)
