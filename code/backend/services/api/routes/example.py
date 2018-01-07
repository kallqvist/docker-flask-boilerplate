from flask import jsonify
from base import APIBase
from services import app


class ExampleEndpointAPI(APIBase):
    """ ExampleEndpointAPI """

    def get(self):
        """
        get example response
        ---
        tags:
            - example
        responses:
            200:
                description: returns an example response
        """
        res = {
            'msg': 'hello world',
        }
        return jsonify(res)

app.add_url_rule('/', view_func=ExampleEndpointAPI.as_view('example_api'))
