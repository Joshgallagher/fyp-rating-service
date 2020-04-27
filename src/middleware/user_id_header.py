import sys

from functools import wraps


def user_id_header(f):
    @wraps(f)
    def inject_user_id(*args, **kwargs):
        print('inject_user_id', file=sys.stderr)
        return f(*args, **kwargs)
    return inject_user_id
