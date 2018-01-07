from flask import request, abort
from flask.views import MethodView


class APIBase(MethodView):
    def get_arg(self, arg, default=None, required=False):
        val = request.args.get(arg, default)
        if required and (arg not in request.args or not val):
            abort(400, "Required parameter '{}' is not set".format(arg))
        return val

    def get_bool_arg(self, arg, default=True, required=False):
        val = self.get_arg(arg, default=default, required=required)
        return bool(
            str(val).lower() == 'true'
        )

    def get_post_data(self):
        if request.form:
            res = request.form
        elif request.json:
            res = request.json
        else:
            res = {}
        return res
