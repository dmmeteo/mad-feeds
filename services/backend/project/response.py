from flask import make_response
from flask import render_template
from flask_mongoengine import BaseQuerySet, Document, DynamicDocument


def make_rss_response(obj, code, headers=None):
    """Makes a Flask response with a XML encoded body"""
    def obj_serialize(o):
        if isinstance(o, Document) or isinstance(o, DynamicDocument):
            return o.to_mongo()
        else:
            return o

    response = make_response(render_template('facebook.xml', obj=[obj_serialize(o) for o in obj]), code)
    response.headers.extend(headers or {"Content-Type": "application/rss+xml; charset=utf-8"})
    return response