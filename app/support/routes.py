from flask import Response
from flask_restful import Resource, reqparse

from . import support_api
from .support import BugReporter

parser_support = reqparse.RequestParser()
parser_support.add_argument(
    'type', type=str, help='bug type', required=True)
parser_support.add_argument(
    'details', type=str, help='bug description', required=True)

bug_reporter = BugReporter()


class Reporter(Resource):
    def post(self):
        args = parser_support.parse_args()
        bug_reporter.report(args)
        return Response(status=200)


support_api.add_resource(Reporter, '/support/')
