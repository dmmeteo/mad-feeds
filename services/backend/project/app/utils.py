from flask import make_response


def as_rss(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        body = f(*args, **kwargs)
        response = make_response(body)
        response.headers["Content-Type"] = "application/rss+xml; charset=utf-8"
        return response
    return decorated_function
