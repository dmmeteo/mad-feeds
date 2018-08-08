from flask_restful import Resource
from project.app.models import Product


class FacebookProductFeed(Resource):

    def get(self):
        products = Product.objects(availability='in stock').paginate(page=1, per_page=2000)
        return products.items, 201