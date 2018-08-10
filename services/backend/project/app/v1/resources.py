from flask_restful import Resource
from project.app.models import Product
from flask_restful.reqparse import RequestParser


class FacebookProductFeed(Resource):

    def get(self):
        args = self.create_parser().parse_args()
        if args['novariants'] == 'no':
            unique = Product.objects.distinct('link')
            products = []
            for u in unique:
                products.append(Product.objects.filter(link=u).first())
            if args['limit']:
                page = 0
                limit = args['limit']
                if args['page']:
                    page = args['page']*limit
                    limit = page+limit
                print(page, limit)
                return products[page:limit], 201
            return products, 201
        else:
            products = Product.objects.paginate(
                page=args.get('page', 1),
                per_page=args['limit']
            )
        return products.items, 201

    @classmethod
    def create_parser(self):
        parser = RequestParser()
        parser.add_argument('page', type=int)
        parser.add_argument('novariants', type=str)
        parser.add_argument('limit', type=int, default=500)
        return parser