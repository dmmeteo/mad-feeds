from flask_restful import Resource


class FacebookProductFeed(Resource):

    def get(self, entry):
        return {'item': entry}