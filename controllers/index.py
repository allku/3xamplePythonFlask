# -*- coding: utf-8 -*-
from flask_restful import Resource


class Index(Resource):
    def get(self):
        return {
            'application': {'name': '3xamplePythonFlask'},
            'success': True
        }
