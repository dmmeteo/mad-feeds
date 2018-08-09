from flask_restful import Resource
from project.app.models import Product
from flask_restful.reqparse import RequestParser


class FacebookProductFeed(Resource):

    def get(self):
        products = Product.objects.paginate(page=1, per_page=2000)
        return products.items, 201

    @classmethod
    def create_parser(self):
        parser = RequestParser()
        parser.add_argument('limit', type=int, default=500)
        parser.add_argument('page', type=int, default=1)